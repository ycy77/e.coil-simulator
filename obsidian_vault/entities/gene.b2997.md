---
entity_id: "gene.b2997"
entity_type: "gene"
name: "hybO"
source_database: "NCBI RefSeq"
source_id: "gene-b2997"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2997"
  - "hybO"
---

# hybO

`gene.b2997`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2997`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hybO (gene.b2997) is a gene entity. It encodes hybO (protein.P69741). Encoded protein function: FUNCTION: This is one of three E.coli hydrogenases synthesized in response to different physiological conditions. HYD2 is involved in hydrogen uptake. EcoCyc product frame: MONOMER0-145. EcoCyc synonyms: yghV. Genomic coordinates: 3145143-3146261. EcoCyc protein note: HybO is the small subunit of hydrogenase 2; sequence analysis suggests it contains three Fe-S clusters; expected to be two [4Fe-4S] and one [3Fe-4S] as has been shown by x-ray crystallography for the small subunit of a Desulfovibrio gigas [Ni-Fe] hydrogenase . HybO contains a twin-arginine signal sequence which is required for membrane targeting by the Tat system. HybO accumulates in a soluble precursor form in a hypB mutant which is unable to insert nickel into the large subunit (HybC) of hydrogenase 2 . HybO and HybC are coordinately assembled and processed; the presence of both subunits, acquisition of the [Ni-Fe] cofactor and subsequent processing of HybC are required for export of the complex by the Tat system . Review:

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), rpoD (protein.P00579), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00633` Nitrotoluene degradation (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69741|protein.P69741]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hybO; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=hybO; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009834,ECOCYC:G7554,GeneID:945902`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3145143-3146261:-; feature_type=gene
