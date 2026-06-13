---
entity_id: "protein.P77172"
entity_type: "protein"
name: "pdeF"
source_database: "UniProt"
source_id: "P77172"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeF yfgF b2503 JW2488"
---

# pdeF

`protein.P77172`

## Static

- Type: `protein`
- Source: `UniProt:P77172`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. Truncated proteins consisting of the GGDEF/EAL domains (residues 319-747) or of the EAL domain alone (481-747) have c-di-GMP phosphodiesterase activity. They do not have diguanylate cyclase activity. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:20522491}.

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991). Component of cyclic di-GMP phosphodiesterase PdeF (complex.ecocyc.CPLX0-8200).

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. Truncated proteins consisting of the GGDEF/EAL domains (residues 319-747) or of the EAL domain alone (481-747) have c-di-GMP phosphodiesterase activity. They do not have diguanylate cyclase activity. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. {ECO:0000269|PubMed:20522491}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52
- `is_component_of` --> [[complex.ecocyc.CPLX0-8200|complex.ecocyc.CPLX0-8200]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2503|gene.b2503]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77172`
- `KEGG:ecj:JW2488;eco:b2503;ecoc:C3026_13880;`
- `GeneID:946968;`
- `GO:GO:0000166; GO:0005886; GO:0016020; GO:0042803; GO:0070301; GO:0071111; GO:0071454; GO:1900190`
- `EC:3.1.4.52`

## Notes

Cyclic di-GMP phosphodiesterase PdeF (EC 3.1.4.52)
