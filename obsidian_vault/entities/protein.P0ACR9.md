---
entity_id: "protein.P0ACR9"
entity_type: "protein"
name: "mprA"
source_database: "UniProt"
source_id: "P0ACR9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mprA emrR b2684 JW2659"
---

# mprA

`protein.P0ACR9`

## Static

- Type: `protein`
- Source: `UniProt:P0ACR9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Negative regulator of the multidrug operon mprA-emrAB (emrRAB) (PubMed:10991887, PubMed:31633764, PubMed:7730261). Binds directly to a promoter in its own operon mprA-emrAB; binding is inhibited by probable inducers of the operon, some of which are also substrates of the efflux pump EmrAB-TolC (PubMed:10991887). {ECO:0000269|PubMed:10991887, ECO:0000269|PubMed:31633764, ECO:0000269|PubMed:7730261}.

## Biological Role

Component of DNA-binding transcriptional repressor MprA (complex.ecocyc.CPLX0-7418).

## Annotation

FUNCTION: Negative regulator of the multidrug operon mprA-emrAB (emrRAB) (PubMed:10991887, PubMed:31633764, PubMed:7730261). Binds directly to a promoter in its own operon mprA-emrAB; binding is inhibited by probable inducers of the operon, some of which are also substrates of the efflux pump EmrAB-TolC (PubMed:10991887). {ECO:0000269|PubMed:10991887, ECO:0000269|PubMed:31633764, ECO:0000269|PubMed:7730261}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7418|complex.ecocyc.CPLX0-7418]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b2684|gene.b2684]] `RegulonDB` `S` - regulator=MprA; target=mprA; function=-
- `represses` --> [[gene.b2685|gene.b2685]] `RegulonDB` `S` - regulator=MprA; target=emrA; function=-
- `represses` --> [[gene.b2686|gene.b2686]] `RegulonDB` `S` - regulator=MprA; target=emrB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2684|gene.b2684]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACR9`
- `KEGG:ecj:JW2659;eco:b2684;ecoc:C3026_14780;`
- `GeneID:93779327;945282;`
- `GO:GO:0003677; GO:0003700; GO:0005829; GO:0006351; GO:0006355; GO:0006950; GO:0045892; GO:0046677`

## Notes

Transcriptional repressor MprA (Transcriptional repressor EmrR)
