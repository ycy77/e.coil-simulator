---
entity_id: "protein.P77495"
entity_type: "protein"
name: "prpE"
source_database: "UniProt"
source_id: "P77495"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prpE yahU b0335 JW0326"
---

# prpE

`protein.P77495`

## Static

- Type: `protein`
- Source: `UniProt:P77495`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of propionyl-CoA from propionate and CoA. Also converts acetate to acetyl-CoA but with a lower specific activity (By similarity). {ECO:0000250}. Propionyl-CoA synthetase catalyzes formation of propinoyl-CoA, the first reaction in propionate catabolism via the methylcitrate cycle. The prpE-encoded propionyl-CoA synthetase contains redox-active thiols that influence enzyme activity. PrpE is activated by DTT, which may reduce an intramolecular disulfide bond between C128 and C315. Like the orthologous enzyme from Salmonella enterica, it may also be activated by removal of a propionyl modification from an active site lysine residue . Overexpression of PrpE has been used as a tool in metabolic engineering of E. coli for heterologous polyketide production . did not detect the PrpE protein in a 2-D gel even during growth on propionate as the sole carbon source; thus, Acs appeared to be more likely than PrpE to catalyze the first step in the propionate metabolism pathway. In addition, showed that a Δacs mutant is unable to grow on propionate as the sole carbon and energy source. Expression of prpE is induced by propionate . Expression of prpBCDE is regulated by PrpR and catabolite repression and is downregulated in the presence of a variety of sugars...

## Biological Role

Catalyzes PROPIONATE--COA-LIGASE-RXN (reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of propionyl-CoA from propionate and CoA. Also converts acetate to acetyl-CoA but with a lower specific activity (By similarity). {ECO:0000250}.

## Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN|reaction.ecocyc.PROPIONATE--COA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0335|gene.b0335]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77495`
- `KEGG:ecj:JW0326;eco:b0335;ecoc:C3026_01640;ecoc:C3026_24810;`
- `GeneID:946891;`
- `GO:GO:0005524; GO:0019629; GO:0050218`
- `EC:6.2.1.17`

## Notes

Propionate--CoA ligase (EC 6.2.1.17) (Propionyl-CoA synthetase)
