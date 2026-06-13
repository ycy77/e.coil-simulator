---
entity_id: "gene.b1749"
entity_type: "gene"
name: "xthA"
source_database: "NCBI RefSeq"
source_id: "gene-b1749"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1749"
  - "xthA"
---

# xthA

`gene.b1749`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1749`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xthA (gene.b1749) is a gene entity. It encodes xthA (protein.P09030). Encoded protein function: FUNCTION: Major apurinic-apyrimidinic endonuclease of E.coli. It removes the damaged DNA at cytosines and guanines by cleaving on the 3'-side of the AP site by a beta-elimination reaction. It exhibits 3'-5'-exonuclease, 3'-phosphomonoesterase, 3'-repair diesterase and ribonuclease H activities. EcoCyc product frame: EG11073-MONOMER. EcoCyc synonyms: xth. Genomic coordinates: 1832428-1833234. EcoCyc protein note: Exonuclease III (XthA) is the major apurinic/apyrimidinic (AP) endonuclease under normal growth conditions; Exonuclease III is a multifunctional enzyme, it displays physiologically important 3' phosphomonoesterase and 3' repair diesterase activity as well as 3' → 5' exonuclease and ribonuclease H activity. Exonuclease III (XthA) was first purified from E. coli strain B and characterised as a 'DNA phosphatase-exonuclease'; active on dsDNA, the enzyme displayed both exonuclease activity (releasing 5' mononucleotides sequentially from the 3'-hydroxyl end of DNA) and 3'-phosphatase activity (releasing inorganic phosphate from 3'-phosphoryl terminated DNA)...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by oxyR (protein.P0ACQ4), rpoS (protein.P13445).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09030|protein.P09030]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB|EcoCyc` `S` - regulator=OxyR; target=xthA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=xthA; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=xthA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005829,ECOCYC:EG11073,GeneID:946254`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1832428-1833234:+; feature_type=gene
