---
entity_id: "gene.b4120"
entity_type: "gene"
name: "melB"
source_database: "NCBI RefSeq"
source_id: "gene-b4120"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4120"
  - "melB"
---

# melB

`gene.b4120`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4120`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

melB (gene.b4120) is a gene entity. It encodes melB (protein.P02921). Encoded protein function: FUNCTION: Mediates the transport of melibiose and other galactosides by a symport mechanism (PubMed:2185831, PubMed:3311166, PubMed:3316227, PubMed:45782, PubMed:7703254). Can use sodium, lithium and protons as coupling cations, depending on the sugar substrate and the cationic environment (PubMed:3311166, PubMed:3316227, PubMed:45782, PubMed:7703254). Alpha-galactosides (melibiose, raffinose, p-nitrophenyl-alpha-galactoside or methyl-alpha-galactoside) are cotransported with either Na(+) or H(+), whereas beta-galactosides (lactose, L-arabinose-beta-D-galactoside, D-fructose-beta-D-galactoside, methyl-beta-galactoside or p-nitrophenyl-beta-galactoside) are cotransported with Na(+) or Li(+) but not H(+) (PubMed:3311166, PubMed:45782). The monosaccharide D-galactose can use either Na(+) or H(+) for cotransport whereas D-fucose, L-arabinose and D-galactosamine can use only Na(+) (PubMed:3311166). {ECO:0000269|PubMed:2185831, ECO:0000269|PubMed:3311166, ECO:0000269|PubMed:3316227, ECO:0000269|PubMed:45782, ECO:0000269|PubMed:7703254}. EcoCyc product frame: MELB-MONOMER. EcoCyc synonyms: mel-4. Genomic coordinates: 4343369-4344790. EcoCyc protein note: MelB is a melibiose-cation cotransport protein belonging to the Glycoside-Pentoside-Hexuronide:Cation Symporter Family (GPH)...

## Biological Role

Repressed by melR (protein.P0ACH8). Activated by rpoD (protein.P00579), melR (protein.P0ACH8), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02921|protein.P02921]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=melB; function=+
- `activates` <-- [[protein.P0ACH8|protein.P0ACH8]] `RegulonDB` `S` - regulator=MelR; target=melB; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=melB; function=+
- `represses` <-- [[protein.P0ACH8|protein.P0ACH8]] `RegulonDB` `S` - regulator=MelR; target=melB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0013495,ECOCYC:EG10578,GeneID:948635`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4343369-4344790:+; feature_type=gene
