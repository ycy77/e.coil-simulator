---
entity_id: "protein.P0A6G5"
entity_type: "protein"
name: "citX"
source_database: "UniProt"
source_id: "P0A6G5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "citX ybdU b0614 JW0606"
---

# citX

`protein.P0A6G5`

## Static

- Type: `protein`
- Source: `UniProt:P0A6G5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transfers 2-(5''-triphosphoribosyl)-3'-dephosphocoenzyme-A on a serine residue to the apo-acyl carrier protein (gamma chain) of the citrate lyase to yield holo-acyl carrier protein. {ECO:0000269|PubMed:10924139, ECO:0000269|PubMed:11042274}. CitX catalyzes the transfer of the citrate lyase prosthetic group 2'-(5''-phosphoribosyl)-3'-dephospho-CoA to the apo-ACP protein of citrate lyase, ACPSUB-MONOMER CitD, converting it to the active holo-ACP form . In vitro, the enzyme also functions as a nucleotidyltransferase . Following the computational prediction of a zinc-binding site in the protein, the presence of the cofactor was verified by ICP-MS. C145, C148, C155 and H161 are involved in metal binding. The presence of the zinc ion confers thermal stability on the protein. Crystal structures were solved by X-ray crystallography at 2.5 Å resolution and by molecular replacement at 1.7 Å resolution, confirming the presence of the zinc ion .

## Biological Role

Catalyzes 2.7.7.61-RXN (reaction.ecocyc.2.7.7.61-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Transfers 2-(5''-triphosphoribosyl)-3'-dephosphocoenzyme-A on a serine residue to the apo-acyl carrier protein (gamma chain) of the citrate lyase to yield holo-acyl carrier protein. {ECO:0000269|PubMed:10924139, ECO:0000269|PubMed:11042274}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.7.61-RXN|reaction.ecocyc.2.7.7.61-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0614|gene.b0614]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6G5`
- `KEGG:ecj:JW0606;eco:b0614;ecoc:C3026_03070;`
- `GeneID:93776871;949084;`
- `GO:GO:0050519; GO:0051191`
- `EC:2.7.7.61`

## Notes

Apo-citrate lyase phosphoribosyl-dephospho-CoA transferase (EC 2.7.7.61) (Apo-ACP nucleodityltransferase) (Holo-ACP synthase) (Holo-citrate lyase synthase)
