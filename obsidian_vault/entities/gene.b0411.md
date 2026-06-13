---
entity_id: "gene.b0411"
entity_type: "gene"
name: "tsx"
source_database: "NCBI RefSeq"
source_id: "gene-b0411"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0411"
  - "tsx"
---

# tsx

`gene.b0411`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0411`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsx (gene.b0411) is a gene entity. It encodes tsx (protein.P0A927). Encoded protein function: FUNCTION: Functions as a substrate-specific channel for nucleosides and deoxynucleosides (PubMed:2458926, PubMed:3276691, PubMed:791677). Has a greater affinity for deoxynucleosides than for nucleosides, and does not transport free bases (PubMed:2458926). In addition, constitutes the receptor for colicin K and phage T6 (PubMed:3276691, PubMed:791677). {ECO:0000269|PubMed:2458926, ECO:0000269|PubMed:3276691, ECO:0000269|PubMed:791677}.; FUNCTION: (Microbial infection) Serves as a receptor for CdiA-STECO31, required for adhesion between E.coli expressing CdiA-STECO31 and this strain. {ECO:0000269|PubMed:28351921}. EcoCyc product frame: EG11035-MONOMER. EcoCyc synonyms: T6rec, nupA. Genomic coordinates: 431129-432013. EcoCyc protein note: Tsx is an outer membrane porin which is responsible for the uptake of nucleosides and deoxynucleosides at sub-uM concentrations . Reconstitution of purified Tsx into lipid bilayer membranes suggests that Tsx has a greater affinity for deoxynucleosides than for nucleosides and that it does not play a role in the transport of nucleobases . Tsx forms a monomeric β-barrel consisting of 12 β strands . In addition to being a channel for (deoxy)nucleosides Tsx functions as a receptor for bacteriophage and colicins and transports the antibiotic, albicidin...

## Biological Role

Repressed by micA (gene.b4442), crp (protein.P0ACJ8), cytR (protein.P0ACN7). Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A927|protein.P0A927]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tsx; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=tsx; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tsx; function=-+
- `represses` <-- [[gene.b4442|gene.b4442]] `RegulonDB` `S` - regulator=MicA; target=tsx; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=tsx; function=-+
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `C` - regulator=CytR; target=tsx; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001425,ECOCYC:EG11035,GeneID:946242`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:431129-432013:-; feature_type=gene
