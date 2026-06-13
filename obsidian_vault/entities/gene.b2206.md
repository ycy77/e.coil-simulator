---
entity_id: "gene.b2206"
entity_type: "gene"
name: "napA"
source_database: "NCBI RefSeq"
source_id: "gene-b2206"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2206"
  - "napA"
---

# napA

`gene.b2206`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2206`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

napA (gene.b2206) is a gene entity. It encodes napA (protein.P33937). Encoded protein function: FUNCTION: Catalytic subunit of the periplasmic nitrate reductase complex NapAB. Receives electrons from NapB and catalyzes the reduction of nitrate to nitrite. {ECO:0000255|HAMAP-Rule:MF_01630, ECO:0000269|PubMed:17130127}. EcoCyc product frame: NAPA-MONOMER. EcoCyc synonyms: yojD, yojC, yojE. Genomic coordinates: 2300267-2302753. EcoCyc protein note: The EG12067 gene encodes the molybdoprotein subunit of the periplasmic nitrate reductase . NapA is synthesized as a precursor with a 36 residue signal peptide that is removed upon export to the periplasm . It binds a CPD-7 "[4Fe-4S]" cluster and CPD-582 . Prior to export the signal peptide of NapA is bound to the EG12143 NapD chaperon, preventing premature export. In the absence of NapD, NapA is unstable and is degraded . A NapD binding epitope is located towards the N-terminus of the NapA signal peptide and partially overlaps with a twin arginine motif . An NMR structure of the NapD-NapA signal peptide complex has been reported .

## Biological Role

Repressed by narL (protein.P0AF28), iscR (protein.P0AGK8), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33937|protein.P33937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=napA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=napA; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=napA; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napA; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=napA; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=napA; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007289,ECOCYC:EG12067,GeneID:947093`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2300267-2302753:-; feature_type=gene
