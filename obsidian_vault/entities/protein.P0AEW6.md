---
entity_id: "protein.P0AEW6"
entity_type: "protein"
name: "gsk"
source_database: "UniProt"
source_id: "P0AEW6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gsk b0477 JW0466"
---

# gsk

`protein.P0AEW6`

## Static

- Type: `protein`
- Source: `UniProt:P0AEW6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of guanosine and inosine to GMP and IMP, respectively (PubMed:10879466, PubMed:7665468, PubMed:7721718). Can also use deoxyguanosine and xanthosine, but not adenosine, uridine, cytidine or deoxythymidine (PubMed:10879466, PubMed:7665468). Shows a strong preference for guanosine (PubMed:10879466, PubMed:7665468). dATP can serve as a phosphate donor as well as ATP. Shows weaker activity with UTP and CTP (PubMed:10879466, PubMed:7665468). {ECO:0000269|PubMed:10879466, ECO:0000269|PubMed:7665468, ECO:0000269|PubMed:7721718}. Inosine-guanosine kinase (Gsk) catalyzes the phosphorylation of inosine and guanosine to IMP and GMP, respectively. It may be involved in the reutilization of endogenously formed nucleosides . Enzymatic activity is higher with guanosine than with inosine as the phosphate acceptor . Product inhibition studies suggest an ordered Bi Bi catalytic mechanism . Guanosine kinase activity of the wild-type gsk allele appears to be insufficient to allow efficient growth of a PRPP-less mutant by utilization of guanosine via the purine salvage pathway . gsk mutant alleles that enable growth on guanosine as the sole source of purine have been indentified . One of the identified mutants, gsk-3, encodes an enzyme that has lost sensitivity to feedback inhibition by GTP...

## Biological Role

Component of inosine/guanosine kinase (complex.ecocyc.CPLX0-322).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of guanosine and inosine to GMP and IMP, respectively (PubMed:10879466, PubMed:7665468, PubMed:7721718). Can also use deoxyguanosine and xanthosine, but not adenosine, uridine, cytidine or deoxythymidine (PubMed:10879466, PubMed:7665468). Shows a strong preference for guanosine (PubMed:10879466, PubMed:7665468). dATP can serve as a phosphate donor as well as ATP. Shows weaker activity with UTP and CTP (PubMed:10879466, PubMed:7665468). {ECO:0000269|PubMed:10879466, ECO:0000269|PubMed:7665468, ECO:0000269|PubMed:7721718}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-322|complex.ecocyc.CPLX0-322]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0477|gene.b0477]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEW6`
- `KEGG:ecj:JW0466;eco:b0477;`
- `GeneID:93776973;946584;`
- `GO:GO:0005524; GO:0006166; GO:0008906; GO:0032263; GO:0032264; GO:0097216; GO:0106366`
- `EC:2.7.1.73`

## Notes

Guanosine-inosine kinase (EC 2.7.1.73)
