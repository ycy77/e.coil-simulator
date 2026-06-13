---
entity_id: "gene.b4093"
entity_type: "gene"
name: "phnO"
source_database: "NCBI RefSeq"
source_id: "gene-b4093"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4093"
  - "phnO"
---

# phnO

`gene.b4093`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4093`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnO (gene.b4093) is a gene entity. It encodes phnO (protein.P16691). Encoded protein function: FUNCTION: Aminoalkylphosphonate N-acetyltransferase which is able to acetylate a range of aminoalkylphosphonic acids, including aminomethylphosphonate, (S)-1-aminoethylphosphonate and 2-aminoethyl- and 3-aminopropylphosphonate, using acetyl-CoA as acetyl donor. Is required for the utilization of aminomethylphosphonate and (S)-1-aminoethylphosphonate as a phosphate source via the C-P lyase pathway. Is also essential for the detoxification of (S)-1-aminoethylphosphonate, a structural analog of D-alanine that has bacteriocidal properties due to inhibition of cell wall synthesis (PubMed:23056305). Also acts as a N-epsilon-lysine acetyltransferase that catalyzes acetylation of several proteins (PubMed:30352934). {ECO:0000269|PubMed:23056305, ECO:0000269|PubMed:30352934}. EcoCyc product frame: EG10724-MONOMER. Genomic coordinates: 4315104-4315538. EcoCyc protein note: PhnO is an aminoalkylphosphonate N-acetyltransferase that is involved in the utilization of aminomethylphosphonate as a source of phosphate. phn+ strains that contain a functional allele of phnE can utilize aminomethylphosphonate (AmMePn), 2-aminoethylphosphonate (2AmEtPn), 3-aminopropylphosphonate (3AmPrPn) as well as methylphosphonate (MePn), ethylphosphonate (EtPn) and propylphosphonate (PrPn) as the source of phosphate...

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16691|protein.P16691]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnO; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013415,ECOCYC:EG10724,GeneID:948599`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4315104-4315538:-; feature_type=gene
