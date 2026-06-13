---
entity_id: "protein.P0ADZ4"
entity_type: "protein"
name: "rpsO"
source_database: "UniProt"
source_id: "P0ADZ4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsO secC b3165 JW3134"
---

# rpsO

`protein.P0ADZ4`

## Static

- Type: `protein`
- Source: `UniProt:P0ADZ4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the primary rRNA binding proteins, it binds directly to 16S rRNA where it helps nucleate assembly of the platform of the 30S subunit by binding and bridging several RNA helices of the 16S rRNA (PubMed:12809609, PubMed:16272117). Binds to its own mRNA, stabilizing it 5-UTR and preventing its translation (PubMed:24339747). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117, ECO:0000269|PubMed:24339747}.; FUNCTION: In the E.coli 70S ribosome it has been modeled (PubMed:12809609) to contact the 23S rRNA of the 50S subunit forming part of bridge B4. In the two 3.5 A resolved ribosome structures (PubMed:16272117) there are minor differences between side-chain conformations. {ECO:0000269|PubMed:12244297, ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}. The S15 protein is a component of the 30S subunit of the ribosome and also functions in the post-transcriptional regulation of its own expression. The S15 protein binds to 16S rRNA in the absence of other ribosomal proteins . Nucleotides essential for the S15-16S rRNA interaction have been determined by mutagenesis and nuclease protection . S15 appears to depend on S4 for assembly . Binding of S8 to 16S rRNA influences the central domain organization and affects the rRNA environment of S15...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the primary rRNA binding proteins, it binds directly to 16S rRNA where it helps nucleate assembly of the platform of the 30S subunit by binding and bridging several RNA helices of the 16S rRNA (PubMed:12809609, PubMed:16272117). Binds to its own mRNA, stabilizing it 5-UTR and preventing its translation (PubMed:24339747). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117, ECO:0000269|PubMed:24339747}.; FUNCTION: In the E.coli 70S ribosome it has been modeled (PubMed:12809609) to contact the 23S rRNA of the 50S subunit forming part of bridge B4. In the two 3.5 A resolved ribosome structures (PubMed:16272117) there are minor differences between side-chain conformations. {ECO:0000269|PubMed:12244297, ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3165|gene.b3165]] `RegulonDB` `C` - regulator=RpsO; target=rpsO; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3165|gene.b3165]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADZ4`
- `KEGG:ecj:JW3134;eco:b3165;ecoc:C3026_17240;`
- `GeneID:89518009;93778818;947686;`
- `GO:GO:0000028; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0006412; GO:0006417; GO:0019843; GO:0022627; GO:0070181`

## Notes

Small ribosomal subunit protein uS15 (30S ribosomal protein S15)
