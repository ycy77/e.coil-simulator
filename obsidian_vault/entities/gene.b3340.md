---
entity_id: "gene.b3340"
entity_type: "gene"
name: "fusA"
source_database: "NCBI RefSeq"
source_id: "gene-b3340"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3340"
  - "fusA"
---

# fusA

`gene.b3340`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3340`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fusA (gene.b3340) is a gene entity. It encodes fusA (protein.P0A6M8). Encoded protein function: FUNCTION: Catalyzes the GTP-dependent ribosomal translocation step during translation elongation (PubMed:8985244). During this step, the ribosome changes from the pre-translocational (PRE) to the post-translocational (POST) state as the newly formed A-site-bound peptidyl-tRNA and P-site-bound deacylated tRNA move to the P and E sites, respectively (PubMed:8985244). Catalyzes the coordinated movement of the two tRNA molecules, the mRNA and conformational changes in the ribosome (PubMed:8985244). {ECO:0000269|PubMed:8985244}. EcoCyc product frame: EG10360-MONOMER. EcoCyc synonyms: far, fus. Genomic coordinates: 3471400-3473514. EcoCyc protein note: Elongation factor G (EF-G) is an essential protein that facilitates the translocation of the ribosome by one codon along the mRNA molecule, shifting the resulting deacylated-tRNA from the ribosomal P-site to the E-site and the peptidyl-tRNA from the A-site to the P-site. The activity requires GTP hydrolysis . EF-G is also involved in ribosome disassembly and recycling . Acetylation site K618 was found to be the key site influencing translational elongation rate but not growth rate . Single molecule analysis revealed structural and kinetic heterogeneity in the ribosome populations...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6M8|protein.P0A6M8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=fusA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010914,ECOCYC:EG10360,GeneID:947847`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3471400-3473514:-; feature_type=gene
