---
entity_id: "gene.b1225"
entity_type: "gene"
name: "narH"
source_database: "NCBI RefSeq"
source_id: "gene-b1225"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1225"
  - "narH"
---

# narH

`gene.b1225`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1225`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narH (gene.b1225) is a gene entity. It encodes narH (protein.P11349). Encoded protein function: FUNCTION: The nitrate reductase enzyme complex allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The beta chain is an electron transfer unit containing four cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit. EcoCyc product frame: NARH-MONOMER. EcoCyc synonyms: chlC. Genomic coordinates: 1283604-1285142. EcoCyc protein note: The β subunit (NarH) of nitrate reductase A contains 4 iron-sulfur clusters - one [3Fe-4S] cluster (FS4) and three [4Fe-4S] clusters (FS1, FS2 and FS3) . FS1, FS2 and FS3 are coordinated by 4 cysteine residues and FS4 is coordinated by 3 cysteine residues (reviewed by . NarH and NarG are significantly upregulated in a ΔCPLX0-245 Ahp strain compared to wild type and redox proteomics indicates that cysteine sites in peptides (NarHCys-217/NarGCys-292) are significantly reduced . nar: nitrate reductase; chl: chlorate resistant

## Biological Role

Activated by fnr (protein.P0A9E5), narL (protein.P0AF28).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P11349|protein.P11349]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=narH; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=narH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004121,ECOCYC:EG10639,GeneID:945780`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1283604-1285142:+; feature_type=gene
