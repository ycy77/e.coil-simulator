---
entity_id: "gene.b0241"
entity_type: "gene"
name: "phoE"
source_database: "NCBI RefSeq"
source_id: "gene-b0241"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0241"
  - "phoE"
---

# phoE

`gene.b0241`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0241`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoE (gene.b0241) is a gene entity. It encodes phoE (protein.P02932). Encoded protein function: FUNCTION: Uptake of inorganic phosphate, phosphorylated compounds, and some other negatively charged solutes. EcoCyc product frame: MONOMER0-282. EcoCyc synonyms: ompE. Genomic coordinates: 259045-260100. EcoCyc protein note: PhoE is a member of the General Bacterial Porin (GBP) family. These proteins are present in the outer membranes of Gram negative bacteria, mitochondria, and plastids. Induced by phosphate limitation, PhoE facilitates efficient diffusion of phosphate and phosphorus-containing compounds across the outer membrane . PhoE specificity is defined by the pore's composition; PhoE is believed to have a preference for small anions due to a collection of positively charged amino acids near the pore entrance . Therefore PhoE is not a specific transport system, rather, it is a water filled channel allowing for passive diffusion of small molecules (~600 Da). Structural studies indicate that PhoE is a trimer of 16-stranded β-barrel monomers with large loops that fold inside the β-barrel, and the amino terminus faces the periplasm . Charged residues within the constriction zone of the pore may act as voltage gating sensors . PhoE activity is inhibited by ATP which blocks ion flow through the porin...

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02932|protein.P02932]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phoE; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=phoE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000823,ECOCYC:EG10729,GeneID:944926`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:259045-260100:-; feature_type=gene
