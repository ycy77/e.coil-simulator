---
entity_id: "protein.P37182"
entity_type: "protein"
name: "hybD"
source_database: "UniProt"
source_id: "P37182"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hybD b2993 JW2961"
---

# hybD

`protein.P37182`

## Static

- Type: `protein`
- Source: `UniProt:P37182`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Protease involved in the C-terminal processing of HybC, the large subunit of hydrogenase 2. Specifically cleaves off a 15 amino acid peptide from the C-terminus of the precursor of HybC. HybD is an endopeptidase involved in the maturation of the large subunit of hydrogenase 2, HYBC-MONOMER HybC . Processing of HybC by HybD is dependent on prior insertion of Fe(CN)2CO. Processing of the HybC C terminus is required for assembly of the catalytically active HybC-HybO heterodimer . HybD was predicted to be the endopeptidase involved in the maturation of HybC based on its similarity to the processing enzyme for hydrogenase 3, HycI . In vitro maturation of FORMHYDROG2-CPLX with protein components including HybD has been achieved . Purified HybD does not contain stoichiometric amounts of bound metal ion . The crystal structure of HybD has been determined at 2.2 Å resolution . A ΔhybD mutant contains unprocessed HybC . Reviews:

## Biological Role

Catalyzes RXN-22655 (reaction.ecocyc.RXN-22655).

## Annotation

FUNCTION: Protease involved in the C-terminal processing of HybC, the large subunit of hydrogenase 2. Specifically cleaves off a 15 amino acid peptide from the C-terminus of the precursor of HybC.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-22655|reaction.ecocyc.RXN-22655]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2993|gene.b2993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37182`
- `KEGG:ecj:JW2961;eco:b2993;ecoc:C3026_16370;`
- `GeneID:948982;`
- `GO:GO:0004175; GO:0004190; GO:0008047; GO:0016485; GO:0046872`
- `EC:3.4.23.-`

## Notes

Hydrogenase 2 maturation protease (EC 3.4.23.-)
