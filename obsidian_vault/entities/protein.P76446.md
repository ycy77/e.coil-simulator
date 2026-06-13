---
entity_id: "protein.P76446"
entity_type: "protein"
name: "pdeN"
source_database: "UniProt"
source_id: "P76446"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdeN rtn b2176 JW2164"
---

# pdeN

`protein.P76446`

## Static

- Type: `protein`
- Source: `UniProt:P76446`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}. PdeN is a predicted c-di-GMP phosphodiesterase; the protein is predicted to contain two transmembrane domains flanking a periplasmic CSS domain containing two highly conserved cysteines, followed by a cytoplasmic C-terminal EAL domain with predicted phosphodiesterase activity . PdeN is one of 5 CSS domain containing c-di-GMP phosphodiesterases in E. coli K-12; redox control and proteolysis of these enzymes is believed to modulate their activity and affect matrix production in biofilm (see ). A screen for suppressors of the motility defect of a EG12252 ΔpdeH mutant identified activating mutations in E. coli's alternative c-di-GMP phosphodiesterases (PDEs), including PdeN. This supports the view that many of the candidate c-di-GMP phosphodiesterases encoded in the E. coli genome require an appropriate stimulus to become active. Suppressor mutations in pdeN consisted of single amino acid substitutions in either the N-terminal membrane sensory domain of PdeN or the EAL catalytic domain and resulted in increased swimming motility and reduced levels of intracellular c-di-GMP . pdeN is expressed during exponential growth in rich media at both 37 and 28°C (see also ). rtn was originally misidentified as a gene of another organism, Proteus vulgaris...

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991).

## Annotation

FUNCTION: Phosphodiesterase (PDE) that catalyzes the hydrolysis of cyclic-di-GMP (c-di-GMP) to 5'-pGpG. {ECO:0000250|UniProtKB:P21514}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52

## Incoming Edges (1)

- `encodes` <-- [[gene.b2176|gene.b2176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76446`
- `KEGG:ecj:JW2164;eco:b2176;ecoc:C3026_12175;`
- `GeneID:946695;`
- `GO:GO:0005886; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Probable cyclic di-GMP phosphodiesterase PdeN (EC 3.1.4.52)
