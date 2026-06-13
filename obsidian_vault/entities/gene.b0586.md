---
entity_id: "gene.b0586"
entity_type: "gene"
name: "entF"
source_database: "NCBI RefSeq"
source_id: "gene-b0586"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0586"
  - "entF"
---

# entF

`gene.b0586`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0586`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entF (gene.b0586) is a gene entity. It encodes entF (protein.P11454). Encoded protein function: FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine (PubMed:1338974, PubMed:1826089, PubMed:216414, PubMed:9485415). EntF catalyzes the activation of L-serine via ATP-dependent PPi exchange reaction to form seryladenylate (PubMed:10688898, PubMed:1338974, PubMed:1826089, PubMed:9485415). Activated L-serine is loaded onto the peptidyl carrier domain via a thioester linkage to the phosphopanthetheine moiety, forming seryl-S-Ppant-EntF (PubMed:9485415). EntF acts then as the sole catalyst for the formation of the three amide and three ester linkages found in enterobactin, using seryladenylate and 2,3-dihydroxybenzoate-S-Ppant-EntB (DHB-S-Ppant-EntB) as substrates, via the formation of a DHB-Ser-S-Ppant-EntF intermediate (PubMed:9485415). {ECO:0000269|PubMed:10688898, ECO:0000269|PubMed:1338974, ECO:0000269|PubMed:1826089, ECO:0000269|PubMed:216414, ECO:0000269|PubMed:9485415}. EcoCyc product frame: MONOMER0-4398. Genomic coordinates: 614157-618038. EcoCyc protein note: ENTF-MONOMER, the entF gene product, activates L-serine through an ATP-pyrophosphate exchange reaction at the carboxylate group of L-serine...

## Biological Role

Repressed by CRP-cyclic-AMP DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-226), fur (protein.P0A9A9). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11454|protein.P11454]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=entF; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=entF; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-226|complex.ecocyc.CPLX0-226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=entF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002021,ECOCYC:EG10264,GeneID:945184`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:614157-618038:+; feature_type=gene
