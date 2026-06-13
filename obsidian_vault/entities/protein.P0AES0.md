---
entity_id: "protein.P0AES0"
entity_type: "protein"
name: "gss"
source_database: "UniProt"
source_id: "P0AES0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gss gsp b2988 JW2956"
---

# gss

`protein.P0AES0`

## Static

- Type: `protein`
- Source: `UniProt:P0AES0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of an amide bond between glutathione (GSH) and spermidine coupled with hydrolysis of ATP; also catalyzes the opposing reaction, i.e. the hydrolysis of glutathionylspermidine (Gsp) back to glutathione and spermidine. The amidase active site can also hydrolyze Gsp-disulfide (Gsp-S-S-Gsp) to Gsp-SG and Gsp S-thiolated proteins (GspSSPs) to GSH S-thiolated protein (GSSPs). Likely acts synergistically with glutaredoxin to regulate the redox environment of E.coli and defend against oxidative damage. In vitro, the amidase active site also catalyzes hydrolysis of amide and ester derivatives of glutathione (e.g. glutathione ethyl ester and glutathione amide) but lacks activity toward acetylspermidine (N1 and N8) and acetylspermine (N1). {ECO:0000269|PubMed:20530482, ECO:0000269|PubMed:23097746, ECO:0000269|PubMed:7775463, ECO:0000269|PubMed:8999955}. gss encodes a bifunctional protein with two domains: an N-terminal glutathionylspermidine (GSP) amidase domain and a C-terminal GSP synthetase domain. The enzyme catalyzes both the formation and hydrolysis of an amide bond between glutathione and spermidine. The net reaction of the two component activities is ATP hydrolysis, a potential futile cycle . Glutathionylspermidine levels in E...

## Biological Role

Component of fused glutathionylspermidine amidase / glutathionylspermidine synthetase (complex.ecocyc.GSP-CPLX).

## Enriched Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of an amide bond between glutathione (GSH) and spermidine coupled with hydrolysis of ATP; also catalyzes the opposing reaction, i.e. the hydrolysis of glutathionylspermidine (Gsp) back to glutathione and spermidine. The amidase active site can also hydrolyze Gsp-disulfide (Gsp-S-S-Gsp) to Gsp-SG and Gsp S-thiolated proteins (GspSSPs) to GSH S-thiolated protein (GSSPs). Likely acts synergistically with glutaredoxin to regulate the redox environment of E.coli and defend against oxidative damage. In vitro, the amidase active site also catalyzes hydrolysis of amide and ester derivatives of glutathione (e.g. glutathione ethyl ester and glutathione amide) but lacks activity toward acetylspermidine (N1 and N8) and acetylspermine (N1). {ECO:0000269|PubMed:20530482, ECO:0000269|PubMed:23097746, ECO:0000269|PubMed:7775463, ECO:0000269|PubMed:8999955}.

## Pathways

- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GSP-CPLX|complex.ecocyc.GSP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2988|gene.b2988]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AES0`
- `KEGG:ecj:JW2956;eco:b2988;ecoc:C3026_16345;`
- `GeneID:93778997;947474;`
- `GO:GO:0005524; GO:0005829; GO:0006749; GO:0008216; GO:0008884; GO:0008885; GO:0046872`
- `EC:3.5.1.78; 6.3.1.8`

## Notes

Bifunctional glutathionylspermidine synthetase/amidase (GspSA) [Includes: Glutathionylspermidine amidase (Gsp amidase) (EC 3.5.1.78) (Glutathionylspermidine amidohydrolase [spermidine-forming]); Glutathionylspermidine synthetase (Gsp synthetase) (EC 6.3.1.8) (Glutathione:spermidine ligase [ADP-forming]) (Gsp synthase)]
