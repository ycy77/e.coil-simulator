---
entity_id: "protein.P76261"
entity_type: "protein"
name: "pdeD"
source_database: "UniProt"
source_id: "P76261"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeD adrB yoaD b1815 JW1804"
---

# pdeD

`protein.P76261`

## Static

- Type: `protein`
- Source: `UniProt:P76261`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (By similarity). May serve as a negative regulator of cellulose synthesis (as has been suggested for S.typhimurium); overexpression inhibits cell aggregation in strains able to produce adhesive curli fimbriae. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria (PubMed:16513732). {ECO:0000250|UniProtKB:P21514, ECO:0000269|PubMed:16513732}. PdeD is a predicted c-di-GMP phosphodiesterase ; it is predicted to be an inner membrane protein with two transmembrane domains which flank a predicted periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeD is one of 5 CSS domain containing c-di-GMP phosphodiesterases in E. coli K-12; redox control and proteolysis of these enzymes is believed to modulate their activity and affect matrix production in biofilm (see ). Expression of pdeD is positively regulated by CsgD. Increased pdeD expression leads to decreased cell aggregation, and conversely, inactivation of pdeD leads to increased cell aggregation, but not increased surface attachment. Inactivation of pdeD may also cause increased production of cellulose...

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG (By similarity). May serve as a negative regulator of cellulose synthesis (as has been suggested for S.typhimurium); overexpression inhibits cell aggregation in strains able to produce adhesive curli fimbriae. Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria (PubMed:16513732). {ECO:0000250|UniProtKB:P21514, ECO:0000269|PubMed:16513732}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52

## Incoming Edges (1)

- `encodes` <-- [[gene.b1815|gene.b1815]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76261`
- `KEGG:ecj:JW1804;eco:b1815;ecoc:C3026_10335;`
- `GeneID:946336;`
- `GO:GO:0005886; GO:0006974; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Probable cyclic di-GMP phosphodiesterase PdeD (EC 3.1.4.52)
