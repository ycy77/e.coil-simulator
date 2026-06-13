---
entity_id: "gene.b2281"
entity_type: "gene"
name: "nuoI"
source_database: "NCBI RefSeq"
source_id: "gene-b2281"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2281"
  - "nuoI"
---

# nuoI

`gene.b2281`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2281`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nuoI (gene.b2281) is a gene entity. It encodes nuoI (protein.P0AFD6). Encoded protein function: FUNCTION: NDH-1 shuttles electrons from NADH, via FMN and iron-sulfur (Fe-S) centers, to quinones in the respiratory chain. The immediate electron acceptor for the enzyme in this species is believed to be ubiquinone. Couples the redox reaction to proton translocation (for every two electrons transferred, four hydrogen ions are translocated across the cytoplasmic membrane), and thus conserves the redox energy in a proton gradient. EcoCyc product frame: NUOI-MONOMER. Genomic coordinates: 2395908-2396450. EcoCyc protein note: NuoI is part of the connecting fragment of NADH dehydrogenase I and is required for efficient assembly of NDH-1 . The Fe-S clusters of NuoI conduct electrons from NuoG to the Fe-S cluster of NuoB . Based on sequence similarity, this subunit was predicted to contain the two 4Fe-4S clusters N6a and N6b . EPR signals for both N6a and N6b have now been detected . Although N6a and N6b are located close to each other, they display no spin-spin interaction . The location and identity of EPR spectra for the N4 and N5 Fe-S clusters were subject of some controversy. The 4Fe-4S cluster N4, located on the NuoG subunit, was thought to be identical to either N6a or N6b...

## Biological Role

Repressed by ryhB (gene.b4451), fnr (protein.P0A9E5), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFD6|protein.P0AFD6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nuoI; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nuoI; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=nuoI; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=nuoI; function=-
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=nuoI; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=nuoI; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007539,ECOCYC:EG12089,GeneID:946757`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2395908-2396450:-; feature_type=gene
