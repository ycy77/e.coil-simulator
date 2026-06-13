---
entity_id: "gene.b2414"
entity_type: "gene"
name: "cysK"
source_database: "NCBI RefSeq"
source_id: "gene-b2414"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2414"
  - "cysK"
---

# cysK

`gene.b2414`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2414`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cysK (gene.b2414) is a gene entity. It encodes cysK (protein.P0ABK5). Encoded protein function: FUNCTION: (Microbial infection) In addition to its role in cysteine synthesis, stimulates the tRNase activity of CdiA-CT from E.coli strain 536 / UPEC; stimulation does not require O-acetylserine sulfhydrylase activity. CdiA is the toxic component of a toxin-immunity protein module, which functions as a cellular contact-dependent growth inhibition (CDI) system. CDI modules allow bacteria to communicate with and inhibit the growth of closely related neighboring bacteria in a contact-dependent fashion (experiments done in strains BW25113 and X90, both K12 derivatives). This protein is not required for CDI of strain EC93, whose toxin may function by forming inner cell membrane pores (PubMed:22333533). CysK stabilizes CdiA-CT, allowing it to bind tRNA substrate; neither CdiA-CT nor CysK bind tRNA alone in vitro (PubMed:27531961). {ECO:0000269|PubMed:22333533, ECO:0000269|PubMed:27531961}. EcoCyc product frame: ACSERLYA-MONOMER. EcoCyc synonyms: ssi5. Genomic coordinates: 2532409-2533380.

## Biological Role

Activated by rpoD (protein.P00579), cysB (protein.P0A9F3).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01320` Sulfur cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABK5|protein.P0ABK5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cysK; function=+
- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=cysK; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007957,ECOCYC:EG10192,GeneID:946877`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2532409-2533380:+; feature_type=gene
