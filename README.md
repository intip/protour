# ProTour

[![Build Status](https://drone.io/github.com/intip/protour/status.png)](https://drone.io/github.com/intip/protour/latest)

Projeto de sites simples de e-commerce de produtos turísticos.

## Instalando

    sudo npm install -g less
    psql -c 'create database test_portalturismo;' -U postgres
    pip install -r project/requirements.txt --use-mirrors
    git submodule init
    git submodule update
    mkdir media
    python manage.py syncdb
    python manage.py migrate_business

## Gerência do projeto

Acessos podem ser requisitados com o Guilherme.

### Pivotal Tracker

[https://www.pivotaltracker.com/s/projects/949780](https://www.pivotaltracker.com/s/projects/949780)

### Trello

[https://trello.com/b/AK23bvh2/protour](https://trello.com/b/AK23bvh2/protour)

Idéias e roadmap. Contribuam entrando cards no inbox, comentando e votando os outros. =)

## Roadmap

### Pré-validação

HTML navegável da home e detalhes do pacote.

### Alpha

Listagem dos podrutos cadastrados usando o business e contato por e-mail.

### Beta

Compra realizada.

### Versão 1.0

Domínio mundial.

## Responsáveis

Guilherme Vierno: [guilherme.vierno@intip.com.br](guilherme.vierno@intip.com.br)
