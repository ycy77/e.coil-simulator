---
entity_id: "protein.P68919"
entity_type: "protein"
name: "rplY"
source_database: "UniProt"
source_id: "P68919"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplY b2185 JW2173"
---

# rplY

`protein.P68919`

## Static

- Type: `protein`
- Source: `UniProt:P68919`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This is one of the proteins that binds to the 5S RNA in the ribosome where it forms part of the central protuberance. Binds to the 5S rRNA independently of L5 and L18. Not required for binding of the 5S rRNA/L5/L18 subcomplex to 23S rRNA. {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:354687, ECO:0000269|PubMed:8925931}. The L25 protein is a component of the 50S subunit of the ribosome and binds to 5S rRNA. L25 is not an essential protein . Binding of L25 to 5S rRNA has been studied in detail . Solution structures of L25 alone and in complex with a segment of 5S rRNA have been determined , and a crystal structure of L25 bound to a loop E-containing fragment of 5S rRNA has been solved at 1.8 Å resolution . The interaction of L25 with 5S rRNA is not required for incorporation of L25 into the ribosome, although it is important for its retention . Molecular dynamics of the main polypeptide Cα-atoms in the α-helices and β-sheets were simulated; the latter have much lower dynamics and higher stability . L25 can be crosslinked to 23S rRNA in the initiation complex and to ribosomal protein L19 . L25 is important for retention of ribosomal protein L16 . A truncated form of L25 can be detected in 2-D gels . L25 is not posttranslationally modified . Although rplY has a non-canonical ribosome binding site, the gene is translated with high efficiency...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: This is one of the proteins that binds to the 5S RNA in the ribosome where it forms part of the central protuberance. Binds to the 5S rRNA independently of L5 and L18. Not required for binding of the 5S rRNA/L5/L18 subcomplex to 23S rRNA. {ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:354687, ECO:0000269|PubMed:8925931}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2185|gene.b2185]] `RegulonDB` `S` - regulator=RplY; target=rplY; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2185|gene.b2185]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P68919`
- `KEGG:ecj:JW2173;eco:b2185;ecoc:C3026_12220;`
- `GeneID:93774996;945618;`
- `GO:GO:0000027; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0006412; GO:0008097; GO:0009314; GO:0017148; GO:0022625`

## Notes

Large ribosomal subunit protein bL25 (50S ribosomal protein L25)
