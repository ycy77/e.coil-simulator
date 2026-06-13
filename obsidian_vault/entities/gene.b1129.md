---
entity_id: "gene.b1129"
entity_type: "gene"
name: "phoQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1129"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1129"
  - "phoQ"
---

# phoQ

`gene.b1129`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1129`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phoQ (gene.b1129) is a gene entity. It encodes phoQ (protein.P23837). Encoded protein function: FUNCTION: Member of the two-component regulatory system PhoP/PhoQ involved in adaptation to low Mg(2+) environments and the control of acid resistance genes (By similarity). Also involved in adaptation to hyperosmotic environments, in a Mg(2+)-independent manner (PubMed:29183977). In low periplasmic Mg(2+), PhoQ functions as a membrane-associated protein kinase that undergoes autophosphorylation and subsequently transfers the phosphate to PhoP, resulting in the expression of PhoP-activated genes (PAG) and repression of PhoP-repressed genes (PRG) (By similarity). In high periplasmic Mg(2+), acts as a protein phosphatase that dephosphorylates phospho-PhoP, resulting in the repression of PAG and may lead to expression of some PRG (By similarity). PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, or treatment with dithiothreitol) (PubMed:22267510). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway; the 2 periplasmic Cys residues of MgrB are required for its action on PhoQ, which then acts on PhoP (PubMed:22267510). Mediates magnesium influx to the cytosol by activation of mgtA (PubMed:10464230)...

## Biological Role

Repressed by micA (gene.b4442), gcvB (gene.b4443), phoP (protein.P23836). Activated by rpoH (protein.P0AGB3), phoP (protein.P23836).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23837|protein.P23837]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=phoQ; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=phoQ; function=-+
- `represses` <-- [[gene.b4442|gene.b4442]] `RegulonDB` `S` - regulator=MicA; target=phoQ; function=-
- `represses` <-- [[gene.b4443|gene.b4443]] `RegulonDB` `S` - regulator=GcvB; target=phoQ; function=-
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=phoQ; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0003805,ECOCYC:EG10732,GeneID:946326`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1188316-1189776:-; feature_type=gene
