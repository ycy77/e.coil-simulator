---
entity_id: "gene.b1011"
entity_type: "gene"
name: "rutB"
source_database: "NCBI RefSeq"
source_id: "gene-b1011"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1011"
  - "rutB"
---

# rutB

`gene.b1011`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1011`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutB (gene.b1011) is a gene entity. It encodes rutB (protein.P75897). Encoded protein function: FUNCTION: Hydrolyzes ureidoacrylate to form aminoacrylate and carbamate. The carbamate hydrolyzes spontaneously, thereby releasing one of the nitrogen atoms of the pyrimidine ring as ammonia and one of its carbon atoms as CO2. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551}. EcoCyc product frame: G6522-MONOMER. EcoCyc synonyms: ycdL. Genomic coordinates: 1072171-1072863. EcoCyc protein note: E. coli K-12 contains a pathway for pyrimidine degradation (PWY0-1471). RutB, which belongs to the isochorismatase family, hydrolyzes ureidoacrylate, the product of the first enzymatic step of the pathway, to generate the unstable intermediates carbamate and aminoacrylate . RutB from E. coli W was purified and appears to be homooctameric in solution . (Note: RutB from E. coli W is 99% identical to RutB from K-12 MG1655.) The enzyme from the K12 strain JM109 was shown to act as a (+)-γ-lactamase, hydrolyzing CPD-26603 efficiently, making it a promising candidate for industrial processes (see CPLX-85455 "enzyme in MetaCyc"). Active site residues were identified and confirmed by alanine scanning mutagenesis . Expression of the rutABCDEFG operon is under the control of nitrogen regulatory protein C (NtrC)...

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by arcA (protein.P0A9Q1), glnG (protein.P0AFB8), nac (protein.Q47005).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75897|protein.P75897]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rutB; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rutB; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=rutB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003414,ECOCYC:G6522,GeneID:945699`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1072171-1072863:-; feature_type=gene
