from django.shortcuts import render
# Create your views here.
from oj import models
import markdown as mk
def questionDetail(request,id):
    question = models.Question.objects.get(questionId=id)
    example = models.Example.objects.get(questionId=id)

    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.footnotes',
        'markdown.extensions.md_in_html',
        'markdown.extensions.tables',
        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.legacy_attrs',
        'markdown.extensions.legacy_em',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        'markdown.extensions.wikilinks'
    ]

    # 问题内容
    questionContent = mk.markdown(question.questionContent, extensions = extensions)
    questionContent = questionContent.replace('<img alt="" src=', '<img alt="" style="width: 40%;" src=')
    questionContent = questionContent.replace('/></p>', '/></p></br>')

    questionTitle = str(question.questionId) + '.' + question.questionTitle

    return render(request,'questionDetail.html',{'question' : question,
                                                 'questionContent' : questionContent,
                                                 'questionTitle' : questionTitle,
                                                 'example' : example,
                                              })