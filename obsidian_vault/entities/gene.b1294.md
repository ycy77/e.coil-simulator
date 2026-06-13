---
entity_id: "gene.b1294"
entity_type: "gene"
name: "sapA"
source_database: "NCBI RefSeq"
source_id: "gene-b1294"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1294"
  - "sapA"
---

# sapA

`gene.b1294`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1294`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sapA (gene.b1294) is a gene entity. It encodes sapA (protein.Q47622). Encoded protein function: FUNCTION: Not part of a putrescine export system (PubMed:27803167). Very similar to a S.typhimurium protein implicated in antimicrobial peptide resistance, but the SapBCDF operon in E.coli is implicated in putrescine export (PubMed:27803167). {ECO:0000269|PubMed:27803167}. EcoCyc product frame: SAPA-MONOMER. Genomic coordinates: 1355467-1357110. EcoCyc protein note: SapA is the periplasmic binding protein of an ATP-binding cassette (ABC)-family transporter complex, SapABCDF, that may be involved in the uptake of a range of molecules, such as AMPs, dipeptides and heme . 'Sap family' transporters are widely present in Gram-negative pathogens where they contribute to resistance against antimicrobial peptides (AMPs) (see ). E. coli K-12 contains a 'consensus' sap operon (sapABCDF) encoding all five Sap components (a substrate binding protein, two membrane proteins and two ATP-binding proteins) in tandem . SapA contains two intramolecular disulfide bonds that contribute to the structural integrity of the protein; purified SapA interacts with Heme-b and with the cationic AMP, Protamines protamine . Separately, in E. coli K-12, CPLX0-13226 SapBCDF (but not SapA) has been implicated in putrescine export...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47622|protein.Q47622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004354,ECOCYC:G2002,GeneID:945873`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1355467-1357110:-; feature_type=gene
