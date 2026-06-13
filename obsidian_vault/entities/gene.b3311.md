---
entity_id: "gene.b3311"
entity_type: "gene"
name: "rpsQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3311"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3311"
  - "rpsQ"
---

# rpsQ

`gene.b3311`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3311`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsQ (gene.b3311) is a gene entity. It encodes rpsQ (protein.P0AG63). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, it binds specifically to the 5'-end of 16S ribosomal RNA (PubMed:4598121). Also plays a role in translational accuracy; neamine-resistant ribosomes show reduced neamine-induced misreading in vitro (PubMed:765484, PubMed:781296). {ECO:0000269|PubMed:4598121, ECO:0000269|PubMed:765484, ECO:0000269|PubMed:781296}. EcoCyc product frame: EG10916-MONOMER. EcoCyc synonyms: neaA. Genomic coordinates: 3448314-3448568. EcoCyc protein note: The S17 protein is a component of the 30S subunit of the ribosome . S17 stabilizes the tertiary structure of the entire 5' domain of 16S rRNA, including non-native folding intermediates . An S17-stabilized non-native folding intermediate appears to be the preferred substrate for EG12044-MONOMER . S17, S4 and S20 together pre-organize the binding site for S16 . Molecular dynamics simulations indicate that binding of S16 rescues the structure of the helix 17 internal loop that is disrupted by previous binding of S17 . The 30S subunit assembly defect due to depleting S17 was analyzed in vivo . S17 binds directly to the 5' domain of 16S rRNA . Specific contact sites have been identified . S17 can also be crosslinked to tRNA in the A site and to the release factor RF-2...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG63|protein.P0AG63]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpsQ; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rpsQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010840,ECOCYC:EG10916,GeneID:947808`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3448314-3448568:-; feature_type=gene
