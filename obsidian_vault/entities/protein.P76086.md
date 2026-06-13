---
entity_id: "protein.P76086"
entity_type: "protein"
name: "paaX"
source_database: "UniProt"
source_id: "P76086"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paaX ydbY b1399 JW1394"
---

# paaX

`protein.P76086`

## Static

- Type: `protein`
- Source: `UniProt:P76086`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Negative regulator of the paaZ and paaABCDEFGHIJK catabolic operons. Binds the consensus sequence 5'-WWTRTGATTCGYGWT-3'. Binding of PaaX is specifically inhibited by phenylacetyl-coenzyme A (PA-CoA). {ECO:0000269|PubMed:10766858, ECO:0000269|PubMed:9748275}.

## Biological Role

Component of PaaX-phenylacetyl-CoA (complex.ecocyc.CPLX0-7729), DNA-binding transcriptional repressor PaaX (complex.ecocyc.CPLX0-7731).

## Annotation

FUNCTION: Negative regulator of the paaZ and paaABCDEFGHIJK catabolic operons. Binds the consensus sequence 5'-WWTRTGATTCGYGWT-3'. Binding of PaaX is specifically inhibited by phenylacetyl-coenzyme A (PA-CoA). {ECO:0000269|PubMed:10766858, ECO:0000269|PubMed:9748275}.

## Outgoing Edges (16)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7729|complex.ecocyc.CPLX0-7729]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7731|complex.ecocyc.CPLX0-7731]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1387|gene.b1387]] `RegulonDB` `C` - regulator=PaaX; target=paaZ; function=-
- `represses` --> [[gene.b1388|gene.b1388]] `RegulonDB` `C` - regulator=PaaX; target=paaA; function=-
- `represses` --> [[gene.b1389|gene.b1389]] `RegulonDB` `C` - regulator=PaaX; target=paaB; function=-
- `represses` --> [[gene.b1390|gene.b1390]] `RegulonDB` `C` - regulator=PaaX; target=paaC; function=-
- `represses` --> [[gene.b1391|gene.b1391]] `RegulonDB` `C` - regulator=PaaX; target=paaD; function=-
- `represses` --> [[gene.b1392|gene.b1392]] `RegulonDB` `C` - regulator=PaaX; target=paaE; function=-
- `represses` --> [[gene.b1393|gene.b1393]] `RegulonDB` `C` - regulator=PaaX; target=paaF; function=-
- `represses` --> [[gene.b1394|gene.b1394]] `RegulonDB` `C` - regulator=PaaX; target=paaG; function=-
- `represses` --> [[gene.b1395|gene.b1395]] `RegulonDB` `C` - regulator=PaaX; target=paaH; function=-
- `represses` --> [[gene.b1396|gene.b1396]] `RegulonDB` `C` - regulator=PaaX; target=paaI; function=-
- `represses` --> [[gene.b1397|gene.b1397]] `RegulonDB` `C` - regulator=PaaX; target=paaJ; function=-
- `represses` --> [[gene.b1398|gene.b1398]] `RegulonDB` `C` - regulator=PaaX; target=paaK; function=-
- `represses` --> [[gene.b1399|gene.b1399]] `RegulonDB` `S` - regulator=PaaX; target=paaX; function=-
- `represses` --> [[gene.b1400|gene.b1400]] `RegulonDB` `S` - regulator=PaaX; target=paaY; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1399|gene.b1399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76086`
- `KEGG:ecj:JW1394;eco:b1399;ecoc:C3026_08160;`
- `GeneID:945966;`
- `GO:GO:0000976; GO:0006351; GO:0010124; GO:2000143`

## Notes

Transcriptional repressor PaaX
