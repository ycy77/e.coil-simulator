---
entity_id: "protein.P0AEJ0"
entity_type: "protein"
name: "emrB"
source_database: "UniProt"
source_id: "P0AEJ0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "emrB b2686 JW2661"
---

# emrB

`protein.P0AEJ0`

## Static

- Type: `protein`
- Source: `UniProt:P0AEJ0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the tripartite efflux system EmrAB-TolC (PubMed:12482849, PubMed:1409590, PubMed:33065135). The system confers resistance to antibiotics such as nalidixic acid and to various hydrophobic compounds, including CCCP, FCCP and 2,4-dinitrophenol (PubMed:12482849, PubMed:1409590, PubMed:33065135). {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590, ECO:0000269|PubMed:33065135}. EmrB is the inner membrane subunit of a tripartite efflux pump that is implicated in the export of a variety of mainly hydrophobic compounds - carbonylcyanide m-chlorophenylhydrazone (CCCP), tetrachlorosalicyanide (TSA), nalidixate, phenylmercury acetate and others (see CPLX0-2121 for more details). emrB encodes a predicted integral inner membrane protein with 14 transmembrane domains; emrB is co-transcribed with emrA - predicted to encode a membrane fusion protein . emrB is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . Swimming motility is increased in the emrB Keio collection mutant (BW25113 ΔemrB::kan) . EmrB is a member of the Drug:H+ Antiporter-2 family within the major facilitator superfamily . emr: E. coli multidrug resistance

## Biological Role

Component of multidrug efflux pump EmrAB-TolC (complex.ecocyc.CPLX0-2121).

## Annotation

FUNCTION: Part of the tripartite efflux system EmrAB-TolC (PubMed:12482849, PubMed:1409590, PubMed:33065135). The system confers resistance to antibiotics such as nalidixic acid and to various hydrophobic compounds, including CCCP, FCCP and 2,4-dinitrophenol (PubMed:12482849, PubMed:1409590, PubMed:33065135). {ECO:0000269|PubMed:12482849, ECO:0000269|PubMed:1409590, ECO:0000269|PubMed:33065135}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2121|complex.ecocyc.CPLX0-2121]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2686|gene.b2686]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEJ0`
- `KEGG:ecj:JW2661;eco:b2686;ecoc:C3026_14790;`
- `GeneID:93779325;947167;`
- `GO:GO:0005886; GO:0009636; GO:0015125; GO:0015721; GO:0022857; GO:0046677; GO:0048545; GO:0055085; GO:0098567; GO:0140330; GO:1990281; GO:1990961`

## Notes

Multidrug export protein EmrB
