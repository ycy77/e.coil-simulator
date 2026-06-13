---
entity_id: "gene.b0635"
entity_type: "gene"
name: "mrdA"
source_database: "NCBI RefSeq"
source_id: "gene-b0635"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0635"
  - "mrdA"
---

# mrdA

`gene.b0635`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0635`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mrdA (gene.b0635) is a gene entity. It encodes mrdA (protein.P0AD65). Encoded protein function: FUNCTION: Catalyzes cross-linking of the peptidoglycan cell wall (PubMed:3009484). Responsible for the determination of the rod shape of the cell (PubMed:1103132). Is probably required for lateral peptidoglycan synthesis and maintenance of the correct diameter during lateral and centripetal growth (PubMed:12519203). {ECO:0000269|PubMed:1103132, ECO:0000269|PubMed:12519203, ECO:0000269|PubMed:3009484}. EcoCyc product frame: EG10606-MONOMER. EcoCyc synonyms: pbpA. Genomic coordinates: 666316-668217. EcoCyc protein note: Penicillin binding protein 2 (PBP2), the product of the mrdA gene is believed to be the primary peptidoglycan (PG) transpeptidase which functions together with the SEDS family protein EG10607-MONOMER MrdB (RodA) to synthesize PG during cell elongation; MrdB-PBP2 are the SEDS-bPBP pair of the elongasome/Rod system. A model of SEDS-bPBP catalysed peptidoglycan synthesis has been generated based on the structural, biochemical, genetic, and computational analyses of a RodA-PBP2 fusion protein . PBP2 displays EG10608-MONOMER "MreB"-like directional motion and has been implicated as the core transpeptidase of peptidoglycan synthesis during cell elongation...

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01501` beta-Lactam resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD65|protein.P0AD65]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=mrdA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002178,ECOCYC:EG10606,GeneID:945240`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:666316-668217:-; feature_type=gene
