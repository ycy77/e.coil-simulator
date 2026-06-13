---
entity_id: "gene.b2203"
entity_type: "gene"
name: "napB"
source_database: "NCBI RefSeq"
source_id: "gene-b2203"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2203"
  - "napB"
---

# napB

`gene.b2203`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2203`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

napB (gene.b2203) is a gene entity. It encodes napB (protein.P0ABL3). Encoded protein function: FUNCTION: Electron transfer subunit of the periplasmic nitrate reductase complex NapAB. Receives electrons from the membrane-anchored tetraheme c-type NapC protein and transfers these to NapA subunit, thus allowing electron flow between membrane and periplasm. Essential for periplasmic nitrate reduction with nitrate as the terminal electron acceptor. {ECO:0000269|PubMed:10234835, ECO:0000269|PubMed:10548535, ECO:0000269|PubMed:17130127}. EcoCyc product frame: NAPB-MONOMER. EcoCyc synonyms: yejY. Genomic coordinates: 2298269-2298718. EcoCyc protein note: The EG12061 gene encodes the periplasmic diheme cytochrome c550 component of the periplasmic nitrate reductase. It receives electrons from the membrane-bound EG12060 NapC protein and passes them to the EG12067 NapA catalytic subunit (and see . E. coli NapA and NapB proteins do not purify as a heterodimeric complex .

## Biological Role

Repressed by narL (protein.P0AF28), iscR (protein.P0AGK8), narP (protein.P31802), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABL3|protein.P0ABL3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=napB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=napB; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=napB; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napB; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=napB; function=-
- `represses` <-- [[protein.P0AGK8|protein.P0AGK8]] `RegulonDB` `S` - regulator=IscR; target=napB; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=napB; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=napB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007283,ECOCYC:EG12061,GeneID:946698`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2298269-2298718:-; feature_type=gene
