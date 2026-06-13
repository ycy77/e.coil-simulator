---
entity_id: "protein.P27245"
entity_type: "protein"
name: "marR"
source_database: "UniProt"
source_id: "P27245"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "marR cfxB inaR soxQ b1530 JW5248"
---

# marR

`protein.P27245`

## Static

- Type: `protein`
- Source: `UniProt:P27245`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the marRAB operon which is involved in the activation of both antibiotic resistance and oxidative stress genes. Binds to the marO operator/promoter site. MarR, "Multiple antibiotic resistance" , participates in controlling several genes involved in resistance to antibiotics , multidrug efflux , oxidative stress , organic solvents , biofilm formation , and heavy metals . The antibiotic resistance associated with MarR appears to involve the acidification of the cytoplasm . MarR is part of the marRAB operon and negatively autoregulates its own expression . The marA gene encodes a transcriptional activator that autoactivates expression of the marRAB operon and that regulates the expression of a global network of at least 80 chromosomal genes . Under laboratory conditions, the marRAB operon can be induced by tetracycline, chloramphenicol, or salicylate , plumbagin, dinitrophenol, and menadione , and other chemicals with phenolic rings . All these compounds attenuate the ability of MarR homodimers to bind their cognate DNA sequences . Cross talk between the mar and rob systems plays an important role in the response to salicylate . In Escherichia coli, the marRAB operon exhibits pulsatile basal expression under non-induced conditions...

## Biological Role

Component of DNA-binding transcriptional repressor MarR (complex.ecocyc.CPLX0-7710), MarR-salicylate (complex.ecocyc.MONOMER-58).

## Annotation

FUNCTION: Repressor of the marRAB operon which is involved in the activation of both antibiotic resistance and oxidative stress genes. Binds to the marO operator/promoter site.

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7710|complex.ecocyc.CPLX0-7710]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.MONOMER-58|complex.ecocyc.MONOMER-58]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1530|gene.b1530]] `RegulonDB` `C` - regulator=MarR; target=marR; function=-
- `represses` --> [[gene.b1531|gene.b1531]] `RegulonDB` `C` - regulator=MarR; target=marA; function=-
- `represses` --> [[gene.b1532|gene.b1532]] `RegulonDB` `C` - regulator=MarR; target=marB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1530|gene.b1530]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27245`
- `KEGG:ecj:JW5248;eco:b1530;ecoc:C3026_08840;`
- `GeneID:945825;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0006950; GO:0009408; GO:0045892; GO:0071236`

## Notes

Multiple antibiotic resistance protein MarR
