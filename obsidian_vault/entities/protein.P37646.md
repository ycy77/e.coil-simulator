---
entity_id: "protein.P37646"
entity_type: "protein"
name: "pdeH"
source_database: "UniProt"
source_id: "P37646"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeH yhjH b3525 JW3493"
---

# pdeH

`protein.P37646`

## Static

- Type: `protein`
- Source: `UniProt:P37646`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the control of the switch from cell motility to adhesion via regulation of cellular levels of cyclic-di-GMP (c-di-GMP) (PubMed:18765794). Part of a signaling cascade that regulates curli biosynthesis. The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA and expression of the master biofilm regulator csgD (PubMed:23708798). Effect on flagella is controlled via the c-di-GMP-binding flagellar brake protein YcgR (PubMed:18765794). {ECO:0000269|PubMed:18765794, ECO:0000269|PubMed:23708798}. Curli amyloid fibers are thin, coiled surface structures composed of a polymer of a single type of subunit, EG11489-MONOMER, encoded by the EG11489 gene . Curli are the key component of the extracellular matrix produced during biofilm formation by Escherichia coli and related Enterobacteriaceae and are involved in inert surface colonization, biofilm formation, and bacterial binding to a variety of extracellular matrix and serum proteins . PdeH is a c-di-GMP phosphodiesterase involved in regulation of the switch from flagellar motility to sessile behavior and curli expression at the end of exponential growth...

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991), RXN0-4181 (reaction.ecocyc.RXN0-4181).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Involved in the control of the switch from cell motility to adhesion via regulation of cellular levels of cyclic-di-GMP (c-di-GMP) (PubMed:18765794). Part of a signaling cascade that regulates curli biosynthesis. The cascade is composed of two c-di-GMP control modules, in which c-di-GMP controlled by the DgcE/PdeH pair (module I) regulates the activity of the DgcM/PdeR pair (module II), which in turn regulates activity of the transcription factor MlrA and expression of the master biofilm regulator csgD (PubMed:23708798). Effect on flagella is controlled via the c-di-GMP-binding flagellar brake protein YcgR (PubMed:18765794). {ECO:0000269|PubMed:18765794, ECO:0000269|PubMed:23708798}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52
- `catalyzes` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3525|gene.b3525]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37646`
- `KEGG:ecj:JW3493;eco:b3525;ecoc:C3026_19095;`
- `GeneID:75173715;75201973;948042;`
- `GO:GO:0000166; GO:0005886; GO:0071111; GO:1900190; GO:1902021`
- `EC:3.1.4.52`

## Notes

Cyclic di-GMP phosphodiesterase PdeH (EC 3.1.4.52)
