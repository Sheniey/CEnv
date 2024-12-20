
# CENV CE @ Sheñey
> **By:** Sheñey [José Daniel]
>
> **License:** GPLv3
>
> **Update:** 28/11/2024 [Updates on: UTC-0]

![CEnv CE' Downloads](https://img.shields.io/github/downloads/Sheniey/CEnv/total)
![CEnv CE's Stars](https://img.shields.io/github/stars/Sheniey/CEnv)
![CEnv CE's Views](https://img.shields.io/github/watchers/Sheniey/CEnv)
![License](https://img.shields.io/github/license/Sheniey/CEnv)
![Last Version](https://img.shields.io/github/v/release/Sheniey/CEnv)
![Last Commit](https://img.shields.io/github/last-commit/Sheniey/CEnv)
![Repo Size](https://img.shields.io/github/repo-size/Sheniey/CEnv)
![@SheñeyBy2010's Subscribers](https://img.shields.io/youtube/channel/subscribers/UCRNf6vOu6FjVbgl5Coqcj_A)
![@SheñeyBy2010's Views](https://img.shields.io/youtube/channel/views/UCRNf6vOu6FjVbgl5Coqcj_A)
![@Sheniey's Stars](https://img.shields.io/github/stars/Sheniey)

---

**The CEnv Documentation in English is Here...**

Follow Me:
1. YouTube: [@Sheñey](https://www.youtube.com/@SheñeyBy2010 "Follow in YouTube |@SheñeyBy2010|")
2. GitHub: [Sheñey](https://www.github.com/Sheniey "Follow in GitHub |Sheñey|")
3. PayPal: [Sheñey](https://www.paypal.com "Support me in PayPal")

---

[**Last Update**](#prerelease-020---29112024 "Goto the Last Update") | [**Unreleased**](#unreleased-100---31112024 "Goto |Unreleased|") | [Released](#released-100---7112024 "Goto the Medium Update") | [Prerelease](#prerelease-000---29112024 "Goto |Prerelease|")

---

## [*] FAQs:
##### [¿Cómo creo un Nuevo Entorno?](#-envsjson)

---

## [+] **Environments** File:
> **Name:** *envs.json*
>
> **Type:** JavaScript Object Notation [JSON]
>
> **Location:**
> ```bash
> /
> └─ src/
>    └─ content/
>       └─ envs.json
> ```
>
> **Function:** DataBase << JSON << "Customs Environments";

Main Structure:
```json
{
    "Section1 Name/": { // just a section
        "Div1 Name/": { // a div or section must ent with '/'
            "Div1 Name/": { // infinity divisions...
                "Environment1 Name": {
                    "attribute": "value" // explicit value
                },
                "Environment2 Name": {
                    "boolAttribute": "booleanValue" // true value || false value
                },
                "Environment3 Name": {
                    "defaultAttribute": null // default value
                },
                "Environment4 Name": {
                    "attributeList": ["value1", "value2", "booleanValue"] // value list
                },
                "Environment4 Name": {
                    "attribute": ["", []] // null | none | void
                }
            }
        },
        "Div2 Name/": {} // void => { will not be shown }
    },
    "Section2 Name/": {} // just another section, void => { will not be shown }
}
```
> [!IMPORTANT]
> Es Recomendable poner en la **"Section"**, areas de la programación o de un ambito principal. Tales como: *Web Develop*, *Script*, *CyberSecurity* o directamente *Books*, *Accounting*, *Movie*, etc.

---

> [!COUTION]
> You Have Reached the End, Turn Around and go Back Immediately!
<br>
