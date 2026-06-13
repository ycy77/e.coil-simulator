---
entity_id: "gene.b4117"
entity_type: "gene"
name: "adiA"
source_database: "NCBI RefSeq"
source_id: "gene-b4117"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4117"
  - "adiA"
---

# adiA

`gene.b4117`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4117`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adiA (gene.b4117) is a gene entity. It encodes adiA (protein.P28629). Encoded protein function: FUNCTION: Component of the acid-resistance (AR) system allowing enteric pathogens to survive the acidic environment in the stomach (Probable). ADC can be found in two forms: biodegradative (this enzyme) and biosynthetic (speA). The biodegradative form plays a role in regulating pH by consuming proteins. Converts arginine imported by AdiC to agmatine which is then exported by AdiC (Probable). {ECO:0000305|PubMed:12867448, ECO:0000305|PubMed:19298070}. EcoCyc product frame: ARGDECARBOXDEG-MONOMER. EcoCyc synonyms: adi. Genomic coordinates: 4338254-4340521.

## Biological Role

Repressed by ydeO (protein.P76135). Activated by rpoD (protein.P00579), adiY (protein.P33234), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28629|protein.P28629]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=adiA; function=+
- `activates` <-- [[protein.P33234|protein.P33234]] `RegulonDB` `S` - regulator=AdiY; target=adiA; function=+
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P76135|protein.P76135]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013483,ECOCYC:EG11501,GeneID:948638`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4338254-4340521:-; feature_type=gene
