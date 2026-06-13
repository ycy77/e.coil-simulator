---
entity_id: "protein.P69937"
entity_type: "protein"
name: "gdx"
source_database: "UniProt"
source_id: "P69937"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:14728684, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:14728684}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gdx sugE b4148 JW5738"
---

# gdx

`protein.P69937`

## Static

- Type: `protein`
- Source: `UniProt:P69937`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:14728684, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:14728684}.

## Enriched Summary

FUNCTION: Guanidinium ion exporter. Couples guanidinium export to the proton motive force, exchanging one guanidinium ion for two protons (PubMed:29507227). Overexpression leads to resistance to a subset of toxic quaternary ammonium compounds such as cetylpyridinium, cetyldimethylethyl ammonium and cetrimide cations (PubMed:11948170). {ECO:0000269|PubMed:11948170, ECO:0000269|PubMed:29507227}.

## Biological Role

Component of guanidinium exporter (complex.ecocyc.CPLX0-8263).

## Annotation

FUNCTION: Guanidinium ion exporter. Couples guanidinium export to the proton motive force, exchanging one guanidinium ion for two protons (PubMed:29507227). Overexpression leads to resistance to a subset of toxic quaternary ammonium compounds such as cetylpyridinium, cetyldimethylethyl ammonium and cetrimide cations (PubMed:11948170). {ECO:0000269|PubMed:11948170, ECO:0000269|PubMed:29507227}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8263|complex.ecocyc.CPLX0-8263]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4148|gene.b4148]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69937`
- `KEGG:ecj:JW5738;eco:b4148;ecoc:C3026_22425;`
- `GeneID:89519135;93777674;948671;`
- `GO:GO:0005886; GO:0006811; GO:0015297; GO:0022857; GO:0055085; GO:1990961`

## Notes

Guanidinium exporter (Quaternary ammonium compound-resistance protein SugE)
