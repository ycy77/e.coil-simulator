---
entity_id: "gene.b2717"
entity_type: "gene"
name: "hycI"
source_database: "NCBI RefSeq"
source_id: "gene-b2717"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2717"
  - "hycI"
---

# hycI

`gene.b2717`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2717`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hycI (gene.b2717) is a gene entity. It encodes hycI (protein.P0AEV9). Encoded protein function: FUNCTION: Protease involved in the C-terminal processing of HycE, the large subunit of hydrogenase 3. {ECO:0000269|PubMed:10727938}. EcoCyc product frame: G7414-MONOMER. Genomic coordinates: 2842573-2843043. EcoCyc protein note: HycI is an endopeptidase that belongs to the M52 peptidase family; it cleaves 32 amino acids off the carboxy-terminus of HYCELARGE-MONOMER HycE, modifying it into its final form as the large subunit of hydrogenase 3 . The substrate HycE must have nickel bound in its center for the processing step to take place . When nickel uptake is blocked, zinc can disrupt HycI proteolysis of HycE, possibly by binding in the nickel site of HycE . HycI shows a somewhat relaxed specificity for amino acid residues at the HycE cleavage site; however, HycI does not cleave a substrate where the C-terminal extension of HycE is swapped for that of HybC . The HycI homolog HyfK from Pectobacterium atrosepticum is able to process the E. coli HycE protein . A high resolution solution structure of the apo form of recombinant HycI was determined by nuclear magnetic resonance spectroscopy . In addition, recombinant HycI was crystallized in the presence of Ca2+ and its crystal structure was determined at 1.70 Å resolution...

## Biological Role

Activated by modE (protein.P0A9G8), fhlA (protein.P19323), rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEV9|protein.P0AEV9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=hycI; function=+
- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hycI; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=hycI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008931,ECOCYC:G7414,GeneID:947428`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2842573-2843043:-; feature_type=gene
