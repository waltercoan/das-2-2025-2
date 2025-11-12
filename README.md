# Design e Arquitetura de Software II 2025/2

[AWS Canvas](https://awsacademy.instructure.com/courses/129676)

## Repositório dos alunos
- [Repos](https://gist.github.com/waltercoan/ccff398b4ecd1899948dcbc1ab78157b)

## Aula 30/07

- Well Architect Framework
- Trade-offs

## Aula 06/08

- Modelo de responsabilidade compartilhada
- Princípio do privilégio mínimo
- Autenticação e Autorização
- IAM User
- IAM Role

## Aula 13/08

- Identity Based Policies
- Resource Based Policies
- [Module 2 Knowledge Check](https://awsacademy.instructure.com/courses/113113/assignments/1270651?module_item_id=10653588)
- [Guided Lab: Exploring AWS Identity and Access Management (IAM)](https://awsacademy.instructure.com/courses/113113/assignments/1270605?module_item_id=10653616)
- [Module 3 Knowledge Check](https://awsacademy.instructure.com/courses/113113/assignments/1270652?module_item_id=10653624)

## Aula 20/08

- Block Storage
- File Share
- Object Store
- S3 resumo geral
- [lab: Creating a Static Website for the Cafe](https://awsacademy.instructure.com/courses/129676/assignments/1485129?module_item_id=12389220)


## Aula 27/08


.vscode/launch.json

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "AWS_ACCESS_KEY_ID": "",
                "AWS_SECRET_ACCESS_KEY": ""
            },
            "envFile": "${workspaceFolder}/.env"
        }
    ]
}
```

## Aula 03/09

- Serviços computacionais da AWS (EC2)
- Amazon Machine Images (AMI)
- Tipos de Instâncias
- Tipos de Storage (EBS/Instance Store)
- Acesso via SSH

## Aula 10/09

- Tipos de Storage (EBS/Instance Store)
- Elastic File System (EFS) / FSx
- EC2 Windows
- [Guided lab: Introducing Amazon Elastic File System (Amazon EFS)](https://awsacademy.instructure.com/courses/129676/assignments/1485164?module_item_id=12389242)


## Aula 17/09

- EC2
  - User Data
  - Instance Metadata
  - Placement
- VPC
  - O que é uma VPC?
  - Subnets Públicas e Privadas
  - Security Group e NACL
  - VPN Site-to-Site
  - Peering

## Aula 24/09

- [Guided lab: Creating a Virtual Private Cloud](https://awsacademy.instructure.com/courses/129676/assignments/1485156?module_item_id=12389305)
- [Challenge (Cafe) lab: Creating a VPC Networking Environment for the Café](https://awsacademy.instructure.com/courses/129676/assignments/1485132?module_item_id=12389306)
- [Module 7 Knowledge Check](https://awsacademy.instructure.com/courses/129676/assignments/1485196?module_item_id=12389310)


# 2 Bimestre

## Aula 08/10/2025
- RBAC x ABAC
- Identidade Federada
- Criptografia Simétrica x Assimétrica
- Detecção de vulnerabilidade estática
- Detecção de intrusão
- [Guided lab: Creating a VPC Peering Connection](https://awsacademy.instructure.com/courses/129676/assignments/1485154?module_item_id=12389321)


## Aula 15/10/2025

- métricas
- logs
- elasticidade
- escalabilidade horizontal
- balanceador de carga
- [Guided lab: Creating a Highly Available Environment](https://awsacademy.instructure.com/courses/129676/assignments/1485152?module_item_id=12389382)


## Aula 22/10/2025

- Module 11: Automating Your Architecture
- [Guided lab: Automating Infrastructure with AWS CloudFormation](https://awsacademy.instructure.com/courses/129676/assignments/1485149?module_item_id=12389414)

## Aula 29/10/2025

- Module 12: Caching Content
- [Module 12 Knowledge Check](https://awsacademy.instructure.com/courses/129676/assignments/1485174?module_item_id=12389441)

## Aula 05/11/2025

- Module 13: Building Decoupled Architectures
- [Guided lab: Building Decoupled Applications by Using Amazon SQS](https://awsacademy.instructure.com/courses/129676/assignments/1485150?module_item_id=12389450)

## Aula 12/11/2025

- Module 14: Building Serverless Architectures and Microservices
- [Guided lab: Implementing a Serverless Architecture on AWS](https://awsacademy.instructure.com/courses/129676/modules/items/12389475)




