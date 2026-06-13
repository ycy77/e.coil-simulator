---
entity_id: "gene.b3362"
entity_type: "gene"
name: "yhfG"
source_database: "NCBI RefSeq"
source_id: "gene-b3362"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3362"
  - "yhfG"
---

# yhfG

`gene.b3362`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3362`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhfG (gene.b3362) is a gene entity. It encodes yhfG (protein.P0ADX5). Encoded protein function: Uncharacterized protein YhfG EcoCyc product frame: EG12374-MONOMER. EcoCyc synonyms: ficA. Genomic coordinates: 3491453-3491620. EcoCyc protein note: Homologs of the E. coli EG10307-MONOMER Fic-FicA proteins act as toxin-antitoxin systems. Fic belongs to a set of enterobacterial FicT homologs with an altered FIC domain signature motif; unlike other FicT proteins, expression of the E. coli protein does not cause a detectable growth defect . Crystal structures of the Fic-FicA complex have been solved. Combined with phylogenetic analysis, the crystal structures show a conserved potential ligand-binding pocket; the ligand awaits identification . A meta-analysis of E. coli K-12 MG1655 transcriptomic data sets in response to multiple stressors found 15 uncharacterized or partially characterized genes (yqfA, yhfG, yhhA, ybgS, arpA, yqaE, yfdY, yaiY, yebE, ydiE, yjcB, yiiX, ycjF, yihF, yidX) that were upregulated under all five stressors: heat, cold, oxidative stress, nitrosative stress, and antibiotic treatment, whereas 3 uncharacterized or partially characterized genes (ymfI, ydiJ, yedE) that were downregulated under all but nitrosative stress . FicA: "FIC domain antitoxin"

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADX5|protein.P0ADX5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=yhfG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010989,ECOCYC:EG12374,GeneID:947871`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3491453-3491620:-; feature_type=gene
