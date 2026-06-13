---
entity_id: "gene.b4125"
entity_type: "gene"
name: "dcuS"
source_database: "NCBI RefSeq"
source_id: "gene-b4125"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4125"
  - "dcuS"
---

# dcuS

`gene.b4125`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4125`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcuS (gene.b4125) is a gene entity. It encodes dcuS (protein.P0AEC8). Encoded protein function: FUNCTION: Member of the two-component regulatory system DcuR/DcuS (PubMed:12167640, PubMed:9765574, PubMed:9973351). Involved in the C4-dicarboxylate-stimulated regulation of the genes encoding the anaerobic fumarate respiratory system (frdABCD; nuoAN; dcuB; sdhCDAB; etc.) (PubMed:9765574, PubMed:9973351). Weakly regulates the aerobic C4-dicarboxylate transporter dctA (PubMed:9973351). Activates DcuR by phosphorylation (PubMed:12167640). {ECO:0000269|PubMed:12167640, ECO:0000269|PubMed:9765574, ECO:0000269|PubMed:9973351}. EcoCyc product frame: PHOSPHO-DCUS-MONOMER. EcoCyc synonyms: yjdH. Genomic coordinates: 4350031-4351662. EcoCyc protein note: Represents the His-349 phosphorylated form of CPLX0-8307 DcuS - the sensor histidine kinase of the DcuSR two-component signal transduction system.

## Biological Role

Repressed by narL (protein.P0AF28). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEC8|protein.P0AEC8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dcuS; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=dcuS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013509,ECOCYC:G7827,GeneID:948639`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4350031-4351662:-; feature_type=gene
