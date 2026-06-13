---
entity_id: "protein.P45463"
entity_type: "protein"
name: "ttdR"
source_database: "UniProt"
source_id: "P45463"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ttdR ygiP b3060 JW3032"
---

# ttdR

`protein.P45463`

## Static

- Type: `protein`
- Source: `UniProt:P45463`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Positive regulator required for L-tartrate-dependent anaerobic growth on glycerol. Induces expression of the ttdA-ttdB-ygjE operon. {ECO:0000269|PubMed:16804186}.

## Biological Role

Component of Dan-L-tartrate DNA-binding transcriptional activator (complex.ecocyc.CPLX0-8048).

## Annotation

FUNCTION: Positive regulator required for L-tartrate-dependent anaerobic growth on glycerol. Induces expression of the ttdA-ttdB-ygjE operon. {ECO:0000269|PubMed:16804186}.

## Outgoing Edges (5)

- `activates` --> [[gene.b3060|gene.b3060]] `RegulonDB` `S` - regulator=Dan; target=ttdR; function=+
- `activates` --> [[gene.b3061|gene.b3061]] `RegulonDB` `S` - regulator=Dan; target=ttdA; function=+
- `activates` --> [[gene.b3062|gene.b3062]] `RegulonDB` `S` - regulator=Dan; target=ttdB; function=+
- `activates` --> [[gene.b3063|gene.b3063]] `RegulonDB` `S` - regulator=Dan; target=ttdT; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8048|complex.ecocyc.CPLX0-8048]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3060|gene.b3060]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45463`
- `KEGG:ecj:JW3032;eco:b3060;ecoc:C3026_16720;`
- `GeneID:93778933;947562;`
- `GO:GO:0001216; GO:0003700; GO:0006351; GO:0043565; GO:0045893`

## Notes

HTH-type transcriptional activator TtdR
