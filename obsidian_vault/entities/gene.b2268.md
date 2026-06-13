---
entity_id: "gene.b2268"
entity_type: "gene"
name: "rbn"
source_database: "NCBI RefSeq"
source_id: "gene-b2268"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2268"
  - "rbn"
---

# rbn

`gene.b2268`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2268`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbn (gene.b2268) is a gene entity. It encodes rbn (protein.P0A8V0). Encoded protein function: FUNCTION: Zinc phosphodiesterase, which has both exoribonuclease and endoribonuclease activities, depending on the nature of the substrate and of the added divalent cation, and on its 3'-terminal structure. Can process the 3' termini of both CCA-less and CCA-containing tRNA precursors. CCA-less tRNAs are cleaved endonucleolytically after the discriminator base, whereas residues following the CCA sequence can be removed exonucleolytically or endonucleolytically in CCA-containing molecules. Does not remove the CCA sequence. May also be involved in the degradation of mRNAs. In vitro, hydrolyzes bis(p-nitrophenyl)phosphate and thymidine-5'-p-nitrophenyl phosphate. {ECO:0000269|PubMed:12029081, ECO:0000269|PubMed:15764599, ECO:0000269|PubMed:16629673, ECO:0000269|PubMed:19366704, ECO:0000269|PubMed:20489203}. EcoCyc product frame: G7175-MONOMER. EcoCyc synonyms: zipD, ecoZ, rnz, elaC. Genomic coordinates: 2381608-2382525.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8V0|protein.P0A8V0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rbn; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007496,ECOCYC:G7175,GeneID:946760`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2381608-2382525:+; feature_type=gene
