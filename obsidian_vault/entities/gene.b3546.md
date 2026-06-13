---
entity_id: "gene.b3546"
entity_type: "gene"
name: "eptB"
source_database: "NCBI RefSeq"
source_id: "gene-b3546"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3546"
  - "eptB"
---

# eptB

`gene.b3546`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3546`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eptB (gene.b3546) is a gene entity. It encodes eptB (protein.P37661). Encoded protein function: FUNCTION: Catalyzes the addition of a phosphoethanolamine (pEtN) moiety to the outer 3-deoxy-D-manno-octulosonic acid (Kdo) residue of a Kdo(2)-lipid A. Phosphatidylethanolamines with one unsaturated acyl group function as pEtN donors and the reaction releases diacylglycerol. {ECO:0000269|PubMed:15795227}. EcoCyc product frame: EG12267-MONOMER. EcoCyc synonyms: yhjW. Genomic coordinates: 3708784-3710475. EcoCyc protein note: EptB catalyses the addition of phosphoethanolamine (pEtN) to the 3-deoxy-d-manno-oct-2-ulosonate (KdoII) sugar of the inner core of lipid A-core oligosaccharide. Lipopolysaccharide, isolated from an E. coli K-12 W3110 derived A-DEEP-ROUGH-FORM-LIPOPOLYSACCHARIDE deep rough (Re) mutant (E. coli WBB06) contains non-stoichiometric pEtN substitutions at position 7 of the second Kdo residue...

## Biological Role

Repressed by arcZ (gene.b4450). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37661|protein.P37661]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=eptB; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=eptB; function=+
- `represses` <-- [[gene.b4450|gene.b4450]] `RegulonDB` `S` - regulator=ArcZ; target=eptB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011581,ECOCYC:EG12267,GeneID:948068`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3708784-3710475:-; feature_type=gene
