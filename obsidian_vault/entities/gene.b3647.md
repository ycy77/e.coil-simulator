---
entity_id: "gene.b3647"
entity_type: "gene"
name: "ligB"
source_database: "NCBI RefSeq"
source_id: "gene-b3647"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3647"
  - "ligB"
---

# ligB

`gene.b3647`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3647`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ligB (gene.b3647) is a gene entity. It encodes ligB (protein.P25772). Encoded protein function: FUNCTION: Catalyzes the formation of phosphodiester linkages between 5'-phosphoryl and 3'-hydroxyl groups in double-stranded DNA using NAD as a coenzyme and as the energy source for the reaction. {ECO:0000269|PubMed:11812821}. EcoCyc product frame: EG11334-MONOMER. EcoCyc synonyms: yicF. Genomic coordinates: 3819488-3821170. EcoCyc protein note: LigB is an NAD+-dependent DNA ligase ; LigB is implicated in base excision repair and/or mismatch repair . Purified LigB ligates a duplex DNA substrate containing a single nick; the reaction requires NAD+ and divalent cations which can be magnesium, manganese, or less effectively cobalt . A ligase-adenylate intermediate is formed when purified LigB is incubated with NAD+ ([32P-AMP]NAD+) and magnesium . LigB has sequence similarity to EG10534-MONOMER "LigA", the other NAD+-dependent DNA ligase in E. coli K-12 . LigB contains the conserved KXDG motif (motif I) which is a signature feature of the ligase/capping superfamily of covalent nucleotidyl transferases ; LigB contains a nucleotidyl transferase domain and oligomer-binding fold (OB-fold) but lacks the BRCT domain and 2 of the 4 zinc-binding cysteines that are characteristic of bacterial NAD+ ligases...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco03030` DNA replication (KEGG)
- `eco03410` Base excision repair (KEGG)
- `eco03420` Nucleotide excision repair (KEGG)
- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25772|protein.P25772]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ligB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011923,ECOCYC:EG11334,GeneID:948164`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3819488-3821170:-; feature_type=gene
