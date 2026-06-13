---
entity_id: "gene.b0053"
entity_type: "gene"
name: "surA"
source_database: "NCBI RefSeq"
source_id: "gene-b0053"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0053"
  - "surA"
---

# surA

`gene.b0053`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0053`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

surA (gene.b0053) is a gene entity. It encodes surA (protein.P0ABZ6). Encoded protein function: FUNCTION: Chaperone involved in the correct folding and assembly of outer membrane proteins, such as OmpA, OmpF and LamB (PubMed:8985185). Recognizes specific patterns of aromatic residues and the orientation of their side chains, which are found more frequently in integral outer membrane proteins (PubMed:8985185). May act in both early periplasmic and late outer membrane-associated steps of protein maturation (PubMed:2165476). Essential for the survival of E.coli in stationary phase. Required for pilus biogenesis (PubMed:16267292). {ECO:0000269|PubMed:16267292, ECO:0000269|PubMed:2165476, ECO:0000269|PubMed:8985185}. EcoCyc product frame: EG10985-MONOMER. Genomic coordinates: 53416-54702. EcoCyc protein note: SurA is a periplasmic chaperone involved in the biogenesis of outer membrane proteins (OMPs). SurA is required for proper assembly of the outer membrane proteins EG10669-MONOMER OmpA, CPLX0-7534 OmpF, and CPLX0-7655 LamB ; loss of SurA is associated with a defective outer membrane and induction of RPOE-MONOMER "σE" activity; surA null mutants show increased sensitivity to detergents, bile salts and some antibiotics (see further ). Depletion of SurA reduces the density of the outer membrane...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABZ6|protein.P0ABZ6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000180,ECOCYC:EG10985,GeneID:944812`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:53416-54702:-; feature_type=gene
