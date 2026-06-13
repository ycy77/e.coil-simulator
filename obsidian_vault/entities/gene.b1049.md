---
entity_id: "gene.b1049"
entity_type: "gene"
name: "opgH"
source_database: "NCBI RefSeq"
source_id: "gene-b1049"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1049"
  - "opgH"
---

# opgH

`gene.b1049`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1049`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

opgH (gene.b1049) is a gene entity. It encodes mdoH (protein.P62517). Encoded protein function: FUNCTION: Involved in the biosynthesis of osmoregulated periplasmic glucans (OPGs). EcoCyc product frame: EG11886-MONOMER. EcoCyc synonyms: mdoA, mdoH. Genomic coordinates: 1110863-1113406. EcoCyc protein note: OpgH is a multifunctional inner membrane protein. OpgH, along with the periplasmic protein OpgG, is required for synthesis of the periplasmic oligosaccharides known as CPD-16398 osmoregulated periplasmic glucans (OPGs), formerly called membrane-derived oligosaccharides (MDOs); although exact details remain unclear, an OpgGH complex is suggested to function for synthesis and translocation of the polyglucose backbone structure of OPG in a process requiring CPD-12575 UDP-glucose and EG50003-MONOMER acyl carrier protein (and see ). OpgH also functions separately and individually as a UDP-glucose-activated inhibitor of cell division; under rich nutrient conditions, OpgH localizes to the division site by an unknown mechanism; OpgH interacts physically with EG10347-MONOMER FtsZ to inhibit cell division...

## Biological Role

Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62517|protein.P62517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=opgH; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=opgH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003560,ECOCYC:EG11886,GeneID:945624`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1110863-1113406:+; feature_type=gene
