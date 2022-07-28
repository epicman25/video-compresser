
from sqlite3 import dbapi2
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cert = {
  "type": "service_account",
  "project_id": "video-1caff",
  "private_key_id": "0dc65f185756822712e5c72f51674cce17ecc534",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDqF/DtPealER+O\nR6jdYkbYeuTSJtUJ9dOUiyC36yKl5jcM8zRDIjLcTLJah5LHd2+ISIj3gQ26SJvY\nBMMOKDlmv4ATXDL0ZepmFdEURLiFNdnIlnwDxjMqypFRKWKPe4KmRC362VmNPewJ\nyzvqQmdPUWBDFHvbmUHaTeKxRzPdP3s8SxVngxT6tBsPUrg9+aSgF+hrGJg5u/V9\nhrYZQVhuls6ulqwpAE9WMvnQbEwzQqP9B0ggm7nzqIsNzd68alAuY7WHCDX8uSq2\nTByfPdrmsDbiuRa3OuIddpn3krTElY7JQdyx4PSr964LAqtopvQ2SwM06hc0A14u\nhPJj4MjFAgMBAAECggEAHLuLitMKOEB9ywzooSOq5m9PHqw9gdd2fMkG3wwxWIOF\nRkWjqInODFQtoAb78RerzOJ6TUa91JuM5VrQRjCRuxbONZIffvfzaUxMOVyl+VO+\nw2wVFLGDHkF2zKtzuYDDbHz518xNvZRYIGudkwdLfuTSF+mvuih5eL4OkQvYRdOE\nyE3fQt6SgjUqpcEzTa0a2bScrEDJiWRo1COIhWZdnQ7Vn0d36rpi74DDLDz74Xhi\ncHPRm9xiHOuoww/nyV41Uxjp1lhiFZdhcGfU5fVYwok6QaB6pPBdfSuDqwcE2dQ/\nuLAJX3fS0MSsWAtUxV0fue0coXykQBX6IAGwnfH5EQKBgQD2D7eccKMx9aMdPq+g\nAeQfL/KEzEEd2AKKihAZEaVxqR0fQV5HCiTG8oH76gRE48uACNxjFX2lQtm1gO68\n2aLvzBk/Rq1v7KmrtTQ/O79J1BdKMC/zu1TTClNvVLpqQ3v3orFfxSW0JxEJhr6e\nunRNarO/5jzysRpBbFVWNE0AGwKBgQDzjHnFk0SJgM/p/ZQquptshnDNYQ4IYQae\nPERvrmg/xbc2jUPgqKZlUmNhi0EyxNPRTz4NJy/3n/Kt35hj6fiu4ut3a7FzgnTb\njt1khi0CHl98tcIoikBdULf0EiWQ38arO/VfBmhvOCfI5s5mBdje1mJ6ujRHn3tv\n0nx6t7SonwKBgEheaQc2zZilARtZ03eA9uIBTRenp0Mqw9yRLJji6sDaFzmZFSxZ\nnGVy763yrtzADpsSgBcYPAL9/V/3kr+yVsymP4qvs9TmSyS4P6yVWvZQzaTBNWk+\n4HzNXaqxxb35KR21GOvs5ODuWIFvwuKWPhyC1GkNQ0GxuuIhBZw796WfAoGBAMTy\nk0KPrbvYG8on0pqfHrKrISskUhm6hISPTfRWQF1ZwKfvorVZDH4hGta1qrqoanX3\ns8ElMGf5w2CR0QTzHrQmMq32u6AiHeey5xu0WU8+So9p2CG6cwRDEw7fYdt+6oRs\nTydR4kAWVC3lX4EnN1I0YZzHWSGWOVabCyidyA0XAoGBAJ0O4EbQkEqnefvBasvZ\n5M7NSoPM31cPj+G+RlJWhc4PN/gp8XJbRA0Lxe/FsngIH7YXGH/A4v2O4GGrfupf\n9UcPI7Ab4NViq7o3XGjHEYrNqjsLrZXscXz8a3vjSW1Q+tw4XJ2NCVlDIUnYK7e0\nJVYLfNjuBqtdzqqIVhaQyafh\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-zs791@video-1caff.iam.gserviceaccount.com",
  "client_id": "104201138721875739221",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zs791%40video-1caff.iam.gserviceaccount.com"
}

cred = credentials.Certificate(cert)
firebase_admin.initialize_app(cred)

db = firestore.client()


