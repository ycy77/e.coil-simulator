---
entity_id: "gene.b2563"
entity_type: "gene"
name: "acpS"
source_database: "NCBI RefSeq"
source_id: "gene-b2563"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2563"
  - "acpS"
---

# acpS

`gene.b2563`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2563`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acpS (gene.b2563) is a gene entity. It encodes acpS (protein.P24224). Encoded protein function: FUNCTION: Transfers the 4'-phosphopantetheine moiety from coenzyme A to the 'Ser-36' of acyl-carrier-protein. {ECO:0000269|PubMed:7559576}. EcoCyc product frame: HOLO-ACP-SYNTH-MONOMER. EcoCyc synonyms: dpj. Genomic coordinates: 2700618-2700998. EcoCyc protein note: The holo-ACP synthase enzyme transfers the 4-phosphopantetheine moeity of CoA to the apo-ACP to form holo-ACP, which is the active form of the carrier in lipid synthesis . The enzyme is a homodimer . The acpS gene is essential for viability . An acpS mutant exhibits growth dependence on supplementation of the media with high levels of pantothenate . Decreased holo-ACP abundance does not affect the rate of incorporation of oleic acid into phospholipid . A conditional acpS mutant (MP4 strain) exhibits an abnormally low ratio of holo-ACP to apo-ACP under permissive as well as restrictive conditions, whereas the ratio of phospholipid to protein content is similar to wild type, indicating that the holo-ACP to apo-ACP ratio is not critical for the maintenance of lipid abundance . This conditional acpS1 mutation from the MP4 strain specifies a G4D change, which decreases enzyme efficiency by 5-fold . The heat sensitivity of an acpS1 mutant is suppressed by overproduction of YhhU...

## Enriched Pathways

- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24224|protein.P24224]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008433,ECOCYC:EG10247,GeneID:947037`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2700618-2700998:-; feature_type=gene
