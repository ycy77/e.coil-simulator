---
entity_id: "gene.b3066"
entity_type: "gene"
name: "dnaG"
source_database: "NCBI RefSeq"
source_id: "gene-b3066"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3066"
  - "dnaG"
---

# dnaG

`gene.b3066`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3066`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dnaG (gene.b3066) is a gene entity. It encodes dnaG (protein.P0ABS5). Encoded protein function: FUNCTION: RNA polymerase that catalyzes the synthesis of short RNA molecules used as primers for DNA polymerase during DNA replication. {ECO:0000255|HAMAP-Rule:MF_00974, ECO:0000269|PubMed:1511009, ECO:0000269|PubMed:340457}. EcoCyc product frame: EG10239-MONOMER. EcoCyc synonyms: dnaP, parB, sdgA. Genomic coordinates: 3211107-3212852. EcoCyc protein note: DNA primase catalyzes the synthesis of RNA primers on single-stranded template DNA . These primers then serve as the starting point for DNA synthesis by DNA polymerase III . Using single-stranded DNA in vitro, primase and NTPs are sufficient to produce RNA primers . In practice, primase also relies on ssDNA-binding protein (SSB) to stabilize its interaction with the primer. The Chi subunit of DNA polymerase III interacts with SSB near the primer, displacing DNA primase and allowing loading of the DNA polymerase III beta sliding clamp . Primase binds three distinct sites during priming, one of them as far as 115 nucleotides distant from the start of primer synthesis . In the case of lagging strand synthesis, primase dissociates from DNA each time an Okazaki fragment is completed and then repeats this binding process to begin priming of the next fragment...

## Biological Role

Repressed by lexA (protein.P0A7C2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABS5|protein.P0ABS5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=dnaG; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=dnaG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010065,ECOCYC:EG10239,GeneID:947570`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3211107-3212852:+; feature_type=gene
