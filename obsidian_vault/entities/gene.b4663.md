---
entity_id: "gene.b4663"
entity_type: "gene"
name: "azuC"
source_database: "NCBI RefSeq"
source_id: "gene-b4663"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4663"
  - "azuC"
---

# azuC

`gene.b4663`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4663`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

azuC (gene.b4663) is a gene entity. It encodes azuC (protein.C1P605). Encoded protein function: Uncharacterized protein AzuC EcoCyc product frame: MONOMER0-2880. Genomic coordinates: 1987873-1987959. EcoCyc protein note: The AzuC coding sequence lies within an RNA initially called G0-17112 IsrB and later AzuCR . AzuCR is a dual-function RNA which can also act as the RNA0-430 AzuR regulatory small RNA. The AzuC coding sequence overlaps the AzuR base-pairing region; AzuC and AzuR activities compete, that is, the mRNA and base-pairing activities of the AzuCR RNA interfere with each other . AzuC interacts with AERGLYC3PDEHYDROG-MONOMER and increases dehydrogenase activity; the physiological relevance of this is uncertain but it may serve to modulate membrane composition . AzuC is predicted to form an amphipathic helix; the protein localizes to the inner membrane . AzuC levels (detected as the sequential peptide affinity (SPA)-tagged protein) are higher in cells grown with glucose compared to those grown with glycerol or galactose due to cAMP receptor protein (CRP)-mediated repression ; AzuC-SPA levels are also repressed under low-oxygen conditions, are moderately induced during heat shock, oxidative stress, and thiol stress, and are substantially increased under acidic (pH 5.5) conditions...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.C1P605|protein.C1P605]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=azuC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285207,ECOCYC:G0-10653,GeneID:7751642`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1987873-1987959:-; feature_type=gene
