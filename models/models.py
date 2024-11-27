from odoo import models, fields, api
from odoo.http import request
import logging
import base64
import os
from odoo.exceptions import ValidationError
_logger = logging.getLogger(__name__)
class JobPosition(models.Model):
    _name = 'job.position'
    _description = 'Job Position'
    _inherit = ['mail.thread', 'mail.activity.mixin']
     
    name = fields.Many2one('job.title', string='Title',tracking=True)
    description = fields.Text(string='Job Description',tracking=True)
    requirements = fields.Many2many('job.skill', string='Skills',tracking=True)
    location = fields.Char(string='Location',tracking=True)
    salary = fields.Monetary(string='Salary Range', currency_field='currency_id',tracking=True)
    currency_id = fields.Many2one('res.currency', string='Currency',tracking=True)
    job_type = fields.Selection([
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ], string='Job Type', required=True,tracking=True)
    openings = fields.Integer(string='Number of Openings', default=1,tracking=True)
    deadline = fields.Date(string='Application Deadline',tracking=True)
    experience_level = fields.Selection([
        ('entry', 'Entry Level'),
        ('mid', 'Mid Level'),
        ('senior', 'Senior Level'),
    ], string='Experience Level',tracking=True)
    posting_date = fields.Date(string='Job Posting Date', default=fields.Date.today,tracking=True)
    status = fields.Selection([
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('on_hold', 'On Hold'),
    ], string='Status', default='open',tracking=True)
    application_ids = fields.One2many('job.application', 'position_id', string='Applications',tracking=True)
    application_count = fields.Integer(string='Applications', compute='_compute_application_count',tracking=True)

    @api.depends('application_ids')
    def _compute_application_count(self):
        for record in self:
            record.application_count = len(record.application_ids)
            

class JobApplication(models.Model):
    _name = 'job.application'
    _description = 'Job Application'

    name = fields.Char(string='Applicant Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number', required=True)
    resume = fields.Binary(string='Resume')
    resume_filename=fields.Char(string='File Name')
    cover_letter = fields.Text(string='Cover Letter')
    status = fields.Selection([
        ('submitted', 'Submitted'),
        ('screening', 'Screening'),
        ('interview', 'Interview'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected')
    ], string='Status', default='submitted', required=True)
    
    position_id = fields.Many2one('job.position', string='Job Position', required=True)
    
    
    
   
    
class JobSkill(models.Model):
    _name = 'job.skill'
    _description = 'Job Skill'

    name = fields.Char(string='Skill', required=True)
    
class JobTitle(models.Model):
    _name = 'job.title'
    _description = 'Job Title'

    name = fields.Char(string='Title', required=True)
    
    
