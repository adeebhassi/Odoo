from odoo import http
from odoo.http import request
import json
import logging
import base64
_logger = logging.getLogger(__name__)
import os
from odoo.exceptions import ValidationError



class JobPositionController(http.Controller):
    @http.route('/myjobs', auth='public',website=True,type='http')
    def get_job_positions(self, **kwargs):
        jobs = request.env['job.position'].search([])
        return request.render('job_posting.index', {
            'jobs': jobs
        })
        
        
    @http.route('/job/detail/<model("job.position"):job>', auth='public', website=True, type='http')
    def job_detail_view(self, job, **kwargs):
        return request.render('job_posting.myjob_detail_view', {
            'job': job
        })
        
    @http.route('''/job/apply/<model("job.position"):job>''', type='http', auth="public", website=True, sitemap=True,)
    def jobs_apply(self, job, **kwargs):
        return request.render("job_posting.job_application_form", {
            'job': job,
        })
        
        
    @http.route('/job/application/submit', auth='public', type='http', methods=['POST'], csrf=False)
    def job_application_submit(self, **kwargs):
        position_id = kwargs.get('position_id')
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        resume = kwargs.get('resume')
        cover_letter = kwargs.get('cover_letter')
        
        if resume:
            resume_data = resume.read()
            resume_filename = resume.filename
        if not position_id or not name or not email or not phone:
            return request.redirect('/job/application/error')
        
        file_extension = os.path.splitext(resume_filename)[1]
        # if file_extension.lower() not in ['.docx', '.pdf', '.txt']:
        #     error_message = "Unsupported file type. Please upload a .docx, .pdf, or .txt file."
        #     return request.redirect('/job/application/error?message=%s' % error_message)
        values ={
            'name': name,
            'email': email,
            'phone': phone,
            'resume':base64.b64encode(resume_data).decode('utf-8') if resume_data else None,
            'resume_filename':resume_filename ,  
            'cover_letter': cover_letter,
            'position_id': position_id,
        }
        application = request.env['job.application'].create(values)
        return request.redirect('/job-thank-you') 

   
    
    
    